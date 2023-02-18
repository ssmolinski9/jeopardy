import random

from loader import Loader

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class CentralWidget(QWidget):

    def __init__(self, points_thresholds, categories):
        super().__init__()
        Loader.load_font()
        self.points_thresholds = points_thresholds
        self.categories = categories 
        self.bonus_positions = random.sample(range(1, len(categories) * len(categories[0].questions) + 1), 2)
        self.setLayout(self.create_layout())

    def create_layout(self):
        layout_grid = QGridLayout()
        self.create_categories_labels(layout_grid)
        self.create_questions_buttons(layout_grid)
        
        return layout_grid 

    def create_categories_labels(self, layout_grid):
        max_width = 0
        for i, category in enumerate(self.categories):
            label = QLabel(category.get_name(), self)
            label.setAlignment(Qt.AlignCenter)
            label.setFont(Loader.global_font)
            layout_grid.addWidget(label, 0, i)
            width = label.fontMetrics().boundingRect(label.text()).width()
            max_width = max(width, max_width)
        for i in range(len(self.categories)):
            layout_grid.setColumnMinimumWidth(i, max_width)

    def create_questions_buttons(self, layout_grid):
        for y, category in enumerate(self.categories):
            for x, question in enumerate(category.get_questions()):
                prize_label = str(self.points_thresholds[x % 5])
                is_bonus = x * len(self.categories) + y + 1 in self.bonus_positions
                button = QuestionButton(question, prize_label, x, y, is_bonus)
                layout_grid.addWidget(button, x + 1, y)


class QuestionButton(QPushButton):
    def __init__(self, question, prize, x, y, is_bonus):
        super().__init__()
        self.question = question
        self.x = x
        self.y = y

        self.setText(prize)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
        self.setStyleSheet("background-color: #00008B; color: white")
        self.setFont(Loader.global_font)
        self.clicked.connect(lambda: self.show_question(is_bonus))

    def show_question(self, is_bonus=False):
        if is_bonus:
            self.show_bonus()
        else:
            self.show_standard()

    def show_bonus(self):
        MessageBox("Bonus!", "How much do you want to play for??")
        self.setText("BONUS")
        self.show_standard()

    def show_standard(self):
        self.setDisabled(True)
        self.setStyleSheet("background-color: gray")
        
        MessageBox("Question", self.question.get_content(), 10000)


class MessageBox(QMessageBox):
    def __init__(self, title, text, time=None):
        super().__init__() 
        self.setSizeGripEnabled(True)
        self.setWindowTitle(title)
        self.setText(text)

        local_font = Loader.global_font
        local_font.setPointSize(38)

        self.setFont(local_font)
        self.layout().setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: #00008B; color: white")

        if time is not None:
            timer = QTimer()
            timer.singleShot(time, self.close)
            timer.start()

        self.resize(800, 600)
        self.showFullScreen()
        self.exec_()

    def event(self, e):
        result = QMessageBox.event(self, e)

        self.setMinimumHeight(0)
        self.setMaximumHeight(16777215)
        self.setMinimumWidth(0)
        self.setMaximumWidth(16777215)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        return result
