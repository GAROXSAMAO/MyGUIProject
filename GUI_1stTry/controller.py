from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

import os, subprocess
from main_ui import Ui_Form

class MainController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)     
        
        # Setup LCD untuk jam real-time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update setiap 1 detik
        self.update_time()
       
        self.button_applications: list[str] = [
            "explorer", "GPT",
            "youtube", "github", "vscode", "python"
        ]
        
        self.ui.pushButton_7.clicked.connect(self.open_applications)
        self.ui.pushButton_8.clicked.connect(self.open_applications)
        self.ui.pushButton_3.clicked.connect(self.open_applications)
        self.ui.pushButton_4.clicked.connect(self.open_applications)
        self.ui.pushButton_5.clicked.connect(self.open_applications)
        self.ui.pushButton_6.clicked.connect(self.open_applications)
       
    def open_applications(self):
        button_id = self.sender()
        
        match button_id:
            # Main big 2 buttons
            case button_id if button_id == self.ui.pushButton_7: os.system("explorer.exe")
            case button_id if button_id == self.ui.pushButton_8: 
                if os.name == 'nt': os.system("start https://chatgpt.com/")
                elif os.name == 'posix': os.system("xdg-open https://chatgpt.com/")
                elif os.name == 'macos': os.system("open https://chatgpt.com/")
            
            # Other 4 small buttons
            case button_id if button_id == self.ui.pushButton_3:
                if os.name == 'nt': os.system("start https://www.youtube.com")
                elif os.name == 'posix': os.system("xdg-open https://www.youtube.com")
                elif os.name == 'macos': os.system("open https://www.youtube.com")
                
            case button_id if button_id == self.ui.pushButton_4:
                if os.name == 'nt': os.system("start https://www.github.com")
                elif os.name == 'posix': os.system("xdg-open https://www.github.com")
                elif os.name == 'macos': os.system("open https://www.github.com")
                
            case button_id if button_id == self.ui.pushButton_5:
                os.name == os.system("code")
                
                
            case button_id if button_id == self.ui.pushButton_6:
                if os.name == 'nt': subprocess.Popen(["start", "cmd", "/k", "python"], shell=True)
                elif os.name == 'posix': subprocess.Popen(["xterm", "-e", "python3"], shell=True)
                elif os.name == 'macos': subprocess.Popen(['osascript', '-e', 'tell application "Terminal" to do script "python3"'], shell=True)

    
    def update_time(self):
        """Update jam di LCD Number."""
        current_time = QTime.currentTime().toString("hh:mm")
        self.ui.lcdCLock.display(current_time)


