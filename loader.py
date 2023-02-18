from category import Category, Question

from PyQt5.QtGui import QFontDatabase, QFont


class Loader:

    global_font = None

    @staticmethod
    def load_points_thresholds():
        with open("data.txt", "r") as f:
            return [int(amount) for amount in f.readline().strip().split(";")]

    @staticmethod
    def load_categories_with_questions():
        categories = []
        with open("data.txt", "r") as f:
            for line in f.readlines()[1:]:
                category, *questions = line.strip().split(";")
                questions = list(map(lambda q: Question(q), questions))
                categories.append(Category(category, questions))
                
        return categories 

    @staticmethod
    def load_font():
        font_db = QFontDatabase() 
        font_id = font_db.addApplicationFont('./font/Quicksand-VariableFont_wght.ttf') 
        font_family = font_db.applicationFontFamilies(font_id)[0]
        Loader.global_font = QFont(font_family)
        Loader.global_font.setPointSize(18)
        return Loader.global_font