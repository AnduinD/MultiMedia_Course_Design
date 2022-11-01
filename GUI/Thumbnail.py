import os,sys,time,threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#私有类
class _ImageListWidget(QListWidget):
    def __init__(self):
        super(_ImageListWidget, self).__init__()
        self.setFlow(QListView.Flow(1))  #QListView.Flow用于控制视图中的数据排列方向，0: 从左到右,1: 从上到下
        self.setIconSize(QSize(150,100))

    def add_image_items(self,image_paths=[]):  #添加图片进入右侧列表
        for img_path in image_paths:
            if os.path.isfile(img_path):
                img_name = os.path.basename(img_path)
                item = QListWidgetItem(QIcon(img_path),img_name)
                # item.setText(img_name)
                # item.setIcon(QIcon(img_path))
                self.addItem(item)


class ImageViewerDialog(QDialog,QThread):   
    def __init__(self,img_dir="E:\HUST学习\大四上\多媒体课设\MultiMedia_Course_Design\test_images"):
        super(QDialog, self).__init__()      
        self.setModal(False)   # 非模态窗体        
        self.list_widget = _ImageListWidget()  #调用私有类
        self.list_widget.setMinimumWidth(200)
        self.list_widget.setMaximumWidth(1000) #限制列表控件的尺寸
        self.show_label = QLabel(self)
        self.show_label.setFixedSize(800,400)
        self.image_paths = []
        self.currentImgIdx = 0
        self.currentImg = None
        self.setWindowIcon(QIcon('./GUI/icon.jpg'))
        self.layout = QHBoxLayout(self)     # 水平布局
        self.layout.addWidget(self.show_label)
        self.layout.addWidget(self.list_widget)

        self.list_widget.itemSelectionChanged.connect(self.loadImage)   #当选中的缩略图发生变化时，链接装载并显示缩略图的槽函数

        try:   
            filenames = os.listdir(img_dir)   #获取图片包含拓展名的全名               
            img_paths=[]                                         
            for file in filenames:  #对每一个图片进行循环                           
                if file[-4:]==".png" or file[-4:]==".jpg" or file[-4:]==".JPG":
                    #若图片文件的最后四个字符，也即扩展名为.jpg或.png，则将对应的图片添加到缩略图列表中          
                    img_paths.append(os.path.join(img_dir,file))       
            self.load_from_paths(img_paths) 
        except Exception as e:  #若文件夹路径无符合特征的图片，则print错误信息
            print("no img_dir{0}".format(img_dir),e)                    
    
        self.setWindowTitle("缩略图预览")
        #self.showMaximized() #窗口化全屏的show
        self.resize(1400,800) 
        self.show()

    def load_from_paths(self,img_paths=[]):
        self.image_paths = img_paths
        self.list_widget.add_image_items(img_paths)

    def loadImage(self):
        self.currentImgIdx = self.list_widget.currentIndex().row()
        if self.currentImgIdx in range(len(self.image_paths)):
            self.currentImg = QPixmap(self.image_paths[self.currentImgIdx]).scaledToHeight(400)
            self.show_label.setPixmap(self.currentImg)
            self.show_label.setAlignment(Qt.AlignCenter) #左侧控件装载并显示图片的缩略图

