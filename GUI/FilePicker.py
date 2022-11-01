import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GUI.Thumbnail import *

class TreeViewDemo(QTreeView):  #QTreeview即pyqt5中提供的树视图控件，可默认生成本机路径树视图
    def __init__(self,path):
        super(TreeViewDemo, self).__init__()
        self.model = QFileSystemModel()
        self.model.setRootPath(path)
        self.model.setFilter(QtCore.QDir.Dirs|QtCore.QDir.NoDotAndDotDot)  #用于筛选树状显示的类型，这里设置只显示文件夹类型
        #为控件添加模式。
        self.setModel(self.model)
        self.setRootIndex(self.model.index(path))  #只显示从GUI_SCD3.py中传入的文件夹路径
        self.doubleClicked.connect(self.thumbnail_display)  #双击绑定显示的某文件夹与缩略图窗体显示创建槽函数

    def thumbnail_display(self,QmodelIndex):
        img_path=self.model.filePath(QmodelIndex)  #缩略图路径继承
        ImageViewerDialog(img_path).exec_() # 创建窗体
    

class TreeViewDialog(QDialog,QThread):       
    def __init__(self,path):                             
        super(QDialog, self).__init__()                 
        self.setModal(False)   #设置为非模态窗体             
        if not os.path.exists(path):
            os.mkdir(path)  #若传入的路径不存在，则在此目录下创建文件夹路径
        self.TreeViewDemo = TreeViewDemo(path)
        self.setWindowIcon(QIcon('./GUI/icon.jpg'))  #设定窗体图标
        self.layout = QHBoxLayout(self)  #树状文件夹窗体水平布局
        self.layout.addWidget(self.TreeViewDemo)
        self.setWindowTitle("文件夹选择") #窗体命名
        self.resize(240,540)  #大小限制
        self.show()