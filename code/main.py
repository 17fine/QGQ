import sys

from PyQt6.QtGui import QPainter, QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt, QResource


QResource.registerResource('app.qrc')


class FullScreenApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)  # 无边框窗口
        self.showFullScreen()  # 显示全屏窗口
        self.setWindowTitle('全屏程序')

        self.setWindowIcon(QIcon('../images/bg.jpg'))

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("../images/bg.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:  # 如果按下的是Q键
            QApplication.quit()  # 退出程序


if __name__ == '__main__':
    app = QApplication(sys.argv)
    full_screen_app = FullScreenApp()
    full_screen_app.show()
    sys.exit(app.exec())
