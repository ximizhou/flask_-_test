import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('尝试一下')

        self.resize(980, 450)

        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()


    sys.exit(app.exec_())