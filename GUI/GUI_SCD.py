# Form implementation generated from reading ui file 'GUI_SCD.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys,os
sys.path.append(".")
import GUI.pic_rc
import GUI.sidepic_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GUI.Thumbnail import ImageViewerDialog
from GUI.FilePicker import TreeViewDialog
from GUI.ProgressBar import ProgressBarDialog
from GUI.ModalError import ModalErrorTextDialog
from HDR_algo.opencv_hdr import hdr_process 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(834, 621)
        MainWindow.resize(834, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listView_BGpic = QtWidgets.QListView(self.centralwidget)
        self.listView_BGpic.setGeometry(QtCore.QRect(0, 0, 841, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_BGpic.sizePolicy().hasHeightForWidth())
        self.listView_BGpic.setSizePolicy(sizePolicy)
        self.listView_BGpic.setStyleSheet("border-image: url(:/picture/bgPic.JPG);")
        self.listView_BGpic.setObjectName("listView_BGpic")

        self.label_Variable1 = QtWidgets.QLabel(self.centralwidget)
        self.label_Variable1.setGeometry(QtCore.QRect(120, 100, 160, 31))
        self.label_Variable1.setStyleSheet("")
        self.label_Variable1.setObjectName("label_Variable1")

        self.pushButton_Process = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Process.setGeometry(QtCore.QRect(540, 100, 160, 81))
        self.pushButton_Process.setStyleSheet("font: 14pt \"黑体\";")
        self.pushButton_Process.setObjectName("pushButton_Process")

        self.label_Title = QtWidgets.QLabel(self.centralwidget)
        self.label_Title.setGeometry(QtCore.QRect(90, 30, 641, 41))
        self.label_Title.setStyleSheet("")
        self.label_Title.setObjectName("label_Title")

        self.label_Variable2 = QtWidgets.QLabel(self.centralwidget)
        self.label_Variable2.setGeometry(QtCore.QRect(120, 150, 160, 31))
        self.label_Variable2.setObjectName("label_Variable2")

        self.pushButton_Thumbnail = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Thumbnail.setGeometry(QtCore.QRect(240, 250, 131, 81))
        self.pushButton_Thumbnail.setStyleSheet("font: 14pt \"黑体\";")
        self.pushButton_Thumbnail.setObjectName("pushButton_Thumbnail")

        self.textEdit_Variable1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Variable1.setGeometry(QtCore.QRect(280, 100, 240, 31))
        self.textEdit_Variable1.setObjectName("textEdit_Variable1")
        self.textEdit_Variable1.setPlainText("Debevec")
        
        self.textEdit_Variable2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Variable2.setGeometry(QtCore.QRect(280, 150, 240, 31))
        self.textEdit_Variable2.setObjectName("textEdit_Variable2")
        self.textEdit_Variable2.setPlainText("Drago")#("default")#

        self.radioButton_Raw = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_Raw.setGeometry(QtCore.QRect(420, 270, 141, 19))
        self.radioButton_Raw.setStyleSheet("font: 9pt \"黑体\";")
        self.radioButton_Raw.setObjectName("radioButton_Raw")
        self.radioButton_Raw.setChecked(True) # 默认选中

        self.radioButton_HDR = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_HDR.setGeometry(QtCore.QRect(420, 300, 141, 19))
        self.radioButton_HDR.setStyleSheet("font: 9pt \"黑体\";")
        self.radioButton_HDR.setObjectName("radioButton_HDR")
        self.radioButton_Raw.setChecked(False) # 默认不选

        self.label_StoragePath = QtWidgets.QLabel(self.centralwidget)
        self.label_StoragePath.setGeometry(QtCore.QRect(120, 200, 160, 31))
        self.label_StoragePath.setObjectName("label_StoragePath")

        self.lineEdit_StoragePath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_StoragePath.setGeometry(QtCore.QRect(280, 200, 240, 31))
        self.lineEdit_StoragePath.setObjectName("lineEdit_StoragePath")
        self.lineEdit_StoragePath.setText(r"./test_images")

        self.pushButton_AdChoose = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AdChoose.setGeometry(QtCore.QRect(540, 200, 131, 31))
        self.pushButton_AdChoose.setStyleSheet("font: 12pt \"黑体\";")
        self.pushButton_AdChoose.setObjectName("pushButton_AdChoose")

        self.listView_sidepic = QtWidgets.QListView(self.centralwidget)
        self.listView_sidepic.setGeometry(QtCore.QRect(10, 10, 131, 81))
        self.listView_sidepic.setStyleSheet("border-image: url(:/hdr/sidepic.png);")
        self.listView_sidepic.setObjectName("listView_sidepic")

        self.listView_BGpic.raise_()
        self.pushButton_Process.raise_()
        self.label_Title.raise_()
        self.label_Variable1.raise_()
        self.label_Variable2.raise_()
        self.pushButton_Thumbnail.raise_()
        self.textEdit_Variable1.raise_()
        self.textEdit_Variable2.raise_()
        self.radioButton_Raw.raise_()
        self.radioButton_HDR.raise_()
        self.label_StoragePath.raise_()
        self.lineEdit_StoragePath.raise_()
        self.pushButton_AdChoose.raise_()
        self.listView_sidepic.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #MainWindow.statusBar().showMessage('广告位招租中！！！')  #状态栏创建
        MainWindow.setWindowIcon(QIcon('./GUI/HDRicon.png'))  #窗体图标创建

        self.pushButton_Thumbnail.clicked.connect(self.ImageViewerDialog_display)  #绑定“图片预览”按钮和对应本机树状存储路径显示槽函数
        self.pushButton_AdChoose.clicked.connect(self.AdBrowse)  #绑定“路径选择”按钮与对应本机文件路径浏览/选择显示的槽函数
        self.pushButton_Process.clicked.connect(self.ProcessThreadCreate) #绑定“处理”按钮与多曝光图像序列融合处理的槽函数

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HDR Converter"))
        self.label_Variable1.setText(_translate("MainWindow",
            """
            <html>
                <head/>
                <body>
                    <p>
                        <span style=\" font-size:8pt;\">
                            CRF & Merge
                        </span>
                    </p>
                </body>
            </html>
            """))
        self.pushButton_Process.setText(_translate("MainWindow", "proc"))
        self.label_Title.setText(_translate("MainWindow", 
            """
            <html>
                <head/>
                <body>
                    <p align=\"center\">
                        <span style=\" font-size:16pt;\">
                            多曝光图像序列融合系统
                        </span>
                    </p>
                </body>
            </html>
            """))
        self.label_Variable2.setText(_translate("MainWindow", 
            """
            <html>
                <head/>
                <body>
                    <p>
                        <span style=\" font-size:8;\">
                            Tone mapping
                        </span>
                    </p>
                </body>
            </html>
            """))
        font = self.pushButton_Thumbnail.font()
        font.setPointSize(8)
        self.pushButton_Thumbnail.setFont(font)
        self.pushButton_Thumbnail.setText(_translate("MainWindow","view"))
        #self.pushButton_Thumbnail.setAlignment(Qt.AlignCenter)
        self.radioButton_Raw.setText(_translate("MainWindow", "待处理图像序列"))
        self.radioButton_HDR.setText(_translate("MainWindow", "输出HDR图像"))
        self.label_StoragePath.setText(_translate("MainWindow", 
            """
            <html>
                <head/>
                <body>
                    <p>
                        <span style=\" font-size:8pt;\">
                            input path
                        </span>
                    </p>
                </body>
            </html>
            """))
        font = self.pushButton_AdChoose.font()
        font.setPointSize(8)
        self.pushButton_AdChoose.setFont(font)
        self.pushButton_AdChoose.setText(_translate("MainWindow", "select"))

    def AdBrowse(self):  #存储路径选择函数
        get_directory_path = QtWidgets.QFileDialog.getExistingDirectory(None,"选取指定文件夹",
                                ".")  #用于获取树状本机全部路径，标题为“选取指定文件夹”，默认从C盘开始
        self.lineEdit_StoragePath.setText(str(get_directory_path))  #将用户选定的路径注入“存储路径”单行文字输入框中

    def ImageViewerDialog_display(self):  #树状路径产生函数，用于图片预览中后续显示缩略图
        if (self.radioButton_Raw.isChecked()):  #预览待处理的图片
            if os.path.exists(self.lineEdit_StoragePath.text()) and (self.lineEdit_StoragePath.text())!=0:
                ImageViewerDialog(self.lineEdit_StoragePath.text()).exec_()
            else:
                ModalErrorTextDialog("路径非法").exec_() #模态框报错
                return   
        elif (self.radioButton_HDR.isChecked()):  #预览处理后的图片
            ImageViewerDialog(r"./HDR_output").exec_()
        else: #若未选择任何选项
            ModalErrorTextDialog("未选择图片预览目录").exec_() #模态框报错
            return

    def ProcessThreadCreate(self):
        if os.path.exists(self.lineEdit_StoragePath.text()) and (self.lineEdit_StoragePath.text())!=0:
            # 进行HDR处理  调用后端程序
            image_dir = self.lineEdit_StoragePath.text()
            merge_method = self.textEdit_Variable1.toPlainText()
            tone_mapping_method = self.textEdit_Variable2.toPlainText()
            print(image_dir)
            hdr_process(image_dir = image_dir,
                        merge_method = merge_method, tone_mapping_method = tone_mapping_method);
        else:
            ModalErrorTextDialog("路径非法").exec_()
            return



class AppMainWindow(QMainWindow):  #主窗体创建函数
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())  #限定主窗体不可拉伸
        self.show()

