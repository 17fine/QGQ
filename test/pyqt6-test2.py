import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class CustomWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口无边框
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # 创建一个容器作为自定义的标题栏
        self.titleBar = QWidget()
        self.titleBarLayout = QVBoxLayout()

        # 创建自定义的关闭按钮
        self.btnClose = QPushButton('X')
        self.btnClose.clicked.connect(self.close)

        # 创建自定义的窗口化按钮
        self.btnMaximize = QPushButton('[]')
        self.btnMaximize.clicked.connect(self.maximizeRestore)

        # 添加按钮到标题栏布局
        self.titleBarLayout.addWidget(self.btnMaximize)
        self.titleBarLayout.addWidget(self.btnClose)
        self.titleBarLayout.addStretch()  # 添加一个伸缩项，让标题栏按钮靠右对齐
        self.titleBar.setLayout(self.titleBarLayout)

        # 创建主窗口的中央部件
        self.centralWidget = QWidget()
        self.centralWidgetLayout = QVBoxLayout()
        self.centralWidgetLayout.addWidget(self.titleBar)  # 将自定义标题栏添加到主布局
        self.centralWidget.setLayout(self.centralWidgetLayout)

        # 设置主窗口的中心部件
        self.setCentralWidget(self.centralWidget)

        # 设置窗口的初始大小
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('自定义窗口按钮示例')

    def maximizeRestore(self):
        if self.isMaximized():
            self.showNormal()
            self.btnMaximize.setText('[]')
        else:
            self.showMaximized()
            self.btnMaximize.setText('[]')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CustomWindow()
    ex.show()
    sys.exit(app.exec())
