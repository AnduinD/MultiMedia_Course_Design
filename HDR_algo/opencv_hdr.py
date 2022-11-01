import os
import cv2
import numpy as np
import piexif
import matplotlib.pyplot as plt

def readImagesAndTimes(image_dir = "./test_images",
                       exposure_list = np.array([0.25, 1/30.0, 2.5, 15.0], dtype=np.float32)):
  filenames = os.listdir(image_dir)

  images = []
  times = []
  # print(len(filenames))
  # print(filenames)

  
  #exposure_list = [] # 如果手动输入的曝光序列和图像序列不匹配，则重新从exif提取曝光
  for idx,filename in enumerate(filenames):
    if os.path.splitext(filename)[1] != '.jpg' and os.path.splitext(filename)[1] != '.JPG':
      print("not an image")
      continue
    filepath = os.path.join(image_dir,filename)#print(filepath)

    if len(exposure_list) != len(filenames): # 从Exif信息中获取曝光时间序列
      exif_dict = piexif.load(filepath)
      exposure_ration = exif_dict["Exif"][33434]  # 通过Exif信息取出曝光时间的元组
      exposure_time = float(exposure_ration[0]/exposure_ration[1]) #, dtype=np.float32)
      times.append(exposure_time)
    else :
      times.append(exposure_list[idx])

    img = cv2.imdecode(np.fromfile(filepath,dtype=np.uint8),-1)
    #cv2.cvtColor(cv2.imdecode(np.fromfile(filepath,dtype=np.uint8),-1),cv2.COLOR_RGB2BGR)
    
    images.append(img) 

    print(f"{filenames[idx]} {times[idx]}")
  #cv2.imshow("test",images[0])

  # print(len(filenames))
  # print(filenames)
  # print(times)
 
  return images, np.asarray(times,np.float32)


def hdr_process(image_dir = "./test_images",
                exposure_list = [],
                merge_method="Debevec",
                tone_mapping_method="default"):
  output_name = "ldr_"+merge_method+"_"+tone_mapping_method+".jpg"

  print("Read images and exposure times ... ")
  if len(exposure_list) : # 加载图像和曝光时间
    images, times = readImagesAndTimes(image_dir,exposure_list)
  else :
    images, times = readImagesAndTimes(image_dir)

  # print(len(images))
  # # 曝光融合 exposure fusion 
  # print("exposure fusion method ... ")
  # merge_mertens = cv2.createMergeMertens()
  # fusion = merge_mertens.process(images)
  # cv2.imwrite('./HDR_output/exposure-fusion.jpg', fusion * 255)
  # print("saved exposure-fusion.jpg")

  if len(times) != len(images):
    # 曝光序列和图像序列不匹配 只进行曝光融合
    print("invalid exposure list")
    merge_method = "Mertens"
    #return

  print("Align input images ... ")
  alignMTB = cv2.createAlignMTB()
  alignMTB.process(images, images)
  
  merge_hdr = None
  if merge_method == "Debevec": 
    print("Calculating Camera Response Function (CRF) ... ")
    calibrate_Debevec = cv2.createCalibrateDebevec(samples=256,lambda_=1.5,random=True) # 估计相机响应
    response_Debevec = calibrate_Debevec.process(images, times)
    response = response_Debevec

    # Merge images into an HDR linear image
    print("Merging images into one HDR image (Debevec)... ")
    merge_Debevec = cv2.createMergeDebevec() # 制作HDR图像
    hdr_Debevec = merge_Debevec.process(images, times, response_Debevec)
    merge_hdr = hdr_Debevec
    cv2.imwrite("./HDR_output/hdrDebevec.hdr", hdr_Debevec)# Save HDR image.
    print("saved hdr_Debevec.hdr ")

  elif merge_method == "Robertson": 
    print("Calculating Camera Response Function (CRF) ... ")
    calibrate_Robertson = cv2.createCalibrateRobertson() # 估计相机响应
    response_Robertson = calibrate_Robertson.process(images, times)
    response = response_Robertson

    print("Merging images into one HDR image (Robertson)... ")
    merge_Robertson = cv2.createMergeRobertson() # 制作HDR图像
    hdr_Robertson = merge_Robertson.process(images, times, response_Robertson)
    merge_hdr = hdr_Robertson
    cv2.imwrite("./HDR_output/hdr_Robertson.jpg", hdr_Robertson)# Save HDR image.
    print("saved hdr_Robertson.hdr ")
  
  elif merge_method == "Mertens":
    # 曝光融合 exposure fusion 
    print("exposure fusion method Mertens ... ")
    merge_mertens = cv2.createMergeMertens()
    fusion = merge_mertens.process(images)
    cv2.imwrite('./HDR_output/ldr_Mertens.jpg', fusion * 255)
    print(np.max(fusion))
    print(np.min(fusion))
    print("saved ldr_Mertens.jpg")
    return

  # #print(response_Debevec.shape)  
  # fig, ax = plt.subplots()
  # ax.plot(range(0,256),response.squeeze())
  # ax.set(xlabel='measured', ylabel='calibrated',title='CRF')
  # ax.grid()
  # fig.savefig("CRF.png")
  # plt.show()



  # 色调映射
  tone_mapping_ldr = None
  if tone_mapping_method == "Drago": 
    print("Tonemaping using Drago's method ... ")
    tonemap_Drago = cv2.createTonemapDrago(1.9,1.0,0.85) #(1.6,0.8 ,0.85)
    ldr_Drago = tonemap_Drago.process(merge_hdr)
    ldr_Drago = 3 * ldr_Drago
    #tone_mapping_ldr = ldr_Drago
    tone_mapping_ldr = np.clip(ldr_Drago*255,0,255).astype(np.uint8)
    # cv2.imwrite("./HDR_output/"+output_name, tone_mapping_ldr)
    # print("saved "+output_name)
    

  elif tone_mapping_method == "Reinhard": 
    print("Tonemaping using Reinhard's method ... ")
    tonemap_Reinhard = cv2.createTonemapReinhard(1.5, 0,0,0)
    ldr_Reinhard = tonemap_Reinhard.process(merge_hdr)
    tone_mapping_ldr = ldr_Reinhard
    tone_mapping_ldr = np.clip(ldr_Reinhard*255,0,255).astype(np.uint8)
    # cv2.imwrite("./HDR_output/"+output_name, ldr_Reinhard * 255)
    # print("saved "+output_name)
    

  elif tone_mapping_method == "Mantiuk": 
    print("Tonemaping using Mantiuk's method ... ")
    tonemap_Mantiuk = cv2.createTonemapMantiuk(2.2,0.85, 1.2)
    ldr_Mantiuk = tonemap_Mantiuk.process(merge_hdr)
    ldr_Mantiuk = 3 * ldr_Mantiuk
    #tone_mapping_ldr = ldr_Mantiuk
    tone_mapping_ldr = np.clip(ldr_Mantiuk*255,0,255).astype(np.uint8)
    # cv2.imwrite("./HDR_output/"+output_name, ldr_Mantiuk * 255)
    # print("saved "+output_name)
    

  else:  #tone_mapping_method == "default" # "Bilateral Filtering": 
    print("Tonemaping using bilateral filtering... ")

    tonemap_bilateral = cv2.createTonemap(2.2)  #2.2
    ldr_bilateral =tonemap_bilateral.process(merge_hdr)
    #ldr_bilateral = merge_hdr
    tone_mapping_ldr = np.clip(ldr_bilateral*255,0,255).astype(np.uint8)

  #print(merge_hdr)
  print(np.max(merge_hdr))
  print(np.min(merge_hdr))  
  cv2.imwrite("./HDR_output/"+output_name, tone_mapping_ldr)
  print("saved "+output_name) 
  print(np.max(tone_mapping_ldr))
  print(np.min(tone_mapping_ldr)) 
  return
  

if __name__ == '__main__':
  print("Read images and exposure times ... ")
  images, times = readImagesAndTimes()# 加载图像和曝光时间
  
  print("Align input images ... ")
  alignMTB = cv2.createAlignMTB()
  alignMTB.process(images, images)
  
  
  print("Calculating Camera Response Function (CRF) ... ")
  calibrateDebevec = cv2.createCalibrateDebevec() # 估计相机响应
  responseDebevec = calibrateDebevec.process(images, times)
  
  # Merge images into an HDR linear image
  print("Merging images into one HDR image ... ")
  mergeDebevec = cv2.createMergeDebevec() # 制作HDR图像
  hdrDebevec = mergeDebevec.process(images, times, responseDebevec)

  cv2.imwrite("hdrDebevec.hdr", hdrDebevec)
  print("saved hdrDebevec.hdr ")# Save HDR image.
  
  # 色调映射
  print("Tonemaping using Drago's method ... ")
  tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
  ldrDrago = tonemapDrago.process(hdrDebevec)
  ldrDrago = 3 * ldrDrago
  cv2.imwrite("ldr-Drago.jpg", ldrDrago * 255)
  print("saved ldr-Drago.jpg")
  
  print("Tonemaping using Reinhard's method ... ")
  tonemapReinhard = cv2.createTonemapReinhard(1.5, 0,0,0)
  ldrReinhard = tonemapReinhard.process(hdrDebevec)
  cv2.imwrite("ldr-Reinhard.jpg", ldrReinhard * 255)
  print("saved ldr-Reinhard.jpg")

  print("Tonemaping using Mantiuk's method ... ")
  tonemapMantiuk = cv2.createTonemapMantiuk(2.2,0.85, 1.2)
  ldrMantiuk = tonemapMantiuk.process(hdrDebevec)
  ldrMantiuk = 3 * ldrMantiuk
  cv2.imwrite("ldr-Mantiuk.jpg", ldrMantiuk * 255)
  print("saved ldr-Mantiuk.jpg")

  print("Tonemaping using bilateral filtering... ")
  tonemap = cv2.createTonemap(2.2)
  ldrBilateralFiltering =tonemap.process(hdrDebevec)
  cv2.imwrite("ldr.jpg", ldrBilateralFiltering * 255)
  print("saved ldr-bilateral-filtering.jpg")

  # 曝光融合 exposure fusion
  merge_mertens = cv2.createMergeMertens()
  fusion = merge_mertens.process(images)
  cv2.imwrite('./HDR_output/exposure-fusion.png', fusion * 255)