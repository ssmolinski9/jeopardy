class Category:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def get_name(self):
        return self.name
    
    def get_questions(self):
        return self.questions


class Question:
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content
