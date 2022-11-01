import sys
sys.path.append(".")
from PyQt5.QtWidgets import QApplication
import GUI.GUI_SCD 
import GlobalVariable as glovar

if __name__ == "__main__":
    glovar._init() 
    app = QApplication(sys.argv)
    mainWindow = GUI.GUI_SCD.AppMainWindow()
    sys.exit(app.exec_())   