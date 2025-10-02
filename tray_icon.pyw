import sys
import os
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon
from noti import *

class SystemTrayApp:
    def __init__(self):
        self.app = QApplication(sys.argv)

        # Khởi tạo tray icon
        self.icon_default = QIcon('noti.ico')
        self.icon_loading = QIcon('loading.ico')
        self.tray = QSystemTrayIcon(self.icon_default, self.app)
        self.tray.setToolTip("Click để check thông báo mới")

        # Menu chuột phải (tùy chọn)
        menu = QMenu()
        setting = menu.addAction("Cài đặt web theo dõi")
        setting.triggered.connect(self.setting)

        menu.addSeparator()

        quit_action = menu.addAction("Thoát")
        quit_action.triggered.connect(self.exit_app)
        self.tray.setContextMenu(menu)

        # Sự kiện click chuột
        self.tray.activated.connect(self.on_click)

        self.tray.show()
        self.tray.setIcon(self.icon_loading)
        main()
        self.tray.setIcon(self.icon_default)
        self.app.exec_()

    def setting(self):
        txt_path = "history_visited.txt"
        os.startfile(txt_path)

    def on_click(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.tray.setIcon(self.icon_loading)
            main()
            self.tray.setIcon(self.icon_default)

    def exit_app(self):
        self.tray.hide()
        self.app.quit()

if __name__ == "__main__":
    SystemTrayApp()