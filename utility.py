class Quiz:
    def __init__(self, name, questions=[]) -> None:
        self.name = name
        self.questions = questions

    def add_questions(self, questions):
        self.questions.extend(questions)

class Question:
    def __init__(self, text, choices=[]) -> None:
        self.text = text
        self.choices = choices

    def add_choices(self, choices):
        self.choices.extend(choices)

class Choice:
    def __init__(self, text, correct=False) -> None:
        self.text = text
        self.correct = correct



