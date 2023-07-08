import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class WorkerThread(QThread):
    finished = pyqtSignal()

    def run(self):
        # 创建标签控件
        label = QLabel("Hello, PyQt5!")

        # 创建主窗口对象
        window = QMainWindow()
        window.setWindowTitle("My PyQt5 Window")
        window.setGeometry(100, 100, 400, 300)
        # 添加标签控件到主窗口
        window.setCentralWidget(label)

        # 显示窗口
        window.show()

        # 发出完成信号
        self.finished.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    thread = WorkerThread()
    thread.finished.connect(app.quit)  # 主线程将在子线程完成时退出
    thread.start()

    sys.exit(app.exec())