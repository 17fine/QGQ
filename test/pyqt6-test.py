import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

# 创建一个应用程序对象
app = QApplication(sys.argv)


# 创建一个窗口
class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 200)
        # 设置窗口的标题
        self.setWindowTitle('PyQt6 简单示例')

        # 创建一个按钮，并设置其位置和大小
        button = QPushButton('点击我', self)
        button.setGeometry(50, 80, 200, 40)

        # 连接按钮的点击信号到我们的槽函数
        button.clicked.connect(self.on_click)

    # 槽函数
    def on_click(self):
        # 显示一个消息框
        QMessageBox.information(self, '信息', '您点击了按钮！')


# 显示窗口
if __name__ == '__main__':
    window = SimpleWindow()
    window.show()
    # 进入应用程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec())
