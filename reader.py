from utility import *
import re


class Reader:
    def __init__(self) -> None:
        self.data = None

    def read_from_file(self, filename:str):
        pass

    def read_from_string(self, string:str):
        pass


class AikenReader(Reader):
    regex = r"(?P<question>.+)\n(?P<choice>(?:[A-Z]\. .+\n)+)ANSWER: (?P<correct>[A-E])\n"
    choice_regex = r"([A-E])\. (.*)"
    def __init__(self) -> None:
        super().__init__()

    def read_from_file(self, filename: str):
        with open(filename) as f:
            self.data = f.read()

        questions = []
        matches = re.finditer(self.regex, self.data, re.MULTILINE)
        for m in matches:
            choice_list = []
            choices = re.findall(self.choice_regex, m["choice"])
            for choice in choices:
                choice_list.append(Choice(
                    choice[1], correct=True if choice[0]==m["correct"] else False
                ))
            questions.append(Question(m["question"], choices=choice_list))

        return Quiz(filename, questions=questions)
            
            



if __name__ == "__main__":
    reader = AikenReader()
    quiz = reader.read_from_file("examples/chapter1.txt")