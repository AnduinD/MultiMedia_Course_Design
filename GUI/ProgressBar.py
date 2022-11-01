# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'processbar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
#import GlobalVariable as glovar

class ProgressBar(QWidget):
    def __init__(self,totalNeedNum):
        super(ProgressBar,self).__init__()
        self.initUI()
        self.totalNeedNum = totalNeedNum  #获取爬取图片数量

    def initUI(self):
        self.resize(300, 200)
        self.pgb = QProgressBar(self)   #载入进度条控件
        self.pgb.move(50, 50)
        self.pgb.resize(250, 20) #设定进度条大小
        self.pgb.setMinimum(0)    
        self.pgb.setMaximum(100)  #设置进度条的范围，最小为0，最大为100
        self.vc = 0    # 配置一个值表示进度条的当前进度
        self.pgb.setValue(self.vc)

        self.timer1 = QBasicTimer()    # 声明一个时钟控件
        self.timer1.start(100, self) # 开始计时器

    def timerEvent(self,event):
        currentGetNum = glovar.get_value("currentGetNum") #从共享变量表获得当前爬取的图片数量
        if self.vc == 100:
            self.timer1.stop()  #若进度已到达100，则停止时钟控件计时
        else:
            self.vc = currentGetNum/self.totalNeedNum*100  #用“当前爬取数量”/“总爬取数量”作为进度条的实时进度
            self.pgb.setValue(int(self.vc))  #给进度条赋值


class ProgressBarDialog(QDialog,QThread):        
    def __init__(self):  
        super(QDialog, self).__init__()          
        self.setModal(True)   # 非模态     
        totalNeedNum = glovar.get_value("totalNeedNum")  ##从共享变量表获得所需爬取的图片总数量
        self.ProgressBar = ProgressBar(totalNeedNum)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.ProgressBar)
        self.setWindowTitle("爬取进度")
        self.resize(400,180)
        self.show()