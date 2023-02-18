import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

from ui import CentralWidget
from loader import Loader


class Jeopardy(QMainWindow):
    def __init__(self):
        super().__init__()
        self.points_thresholds = Loader.load_points_thresholds()
        self.categories = Loader.load_categories_with_questions()
        self.init_ui()
        self.showFullScreen()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def init_ui(self):
        self.setWindowTitle("Jeopardy Game")
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(CentralWidget(self.points_thresholds, self.categories))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Jeopardy()
    sys.exit(app.exec_())