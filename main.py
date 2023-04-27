import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeWidgetItem, QMessageBox
from PySide2.QtGui import QColor
from image_creator import ImageCreator, Settings
from reader import AikenReader
from ui_mainwindow import Ui_MainWindow
import matplotlib.font_manager
from pygments.styles import get_all_styles
import os

from writer import XMLSaver


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.openFileButton.clicked.connect(self.open)
        self.exportButton.clicked.connect(self.export)
        self.previewSettingsButton.clicked.connect(self.preview)
        self.fill_fonts()
        self.fill_code_styles()
        self.setupQTreeWidget()
        self.quiz = None


    def open(self):
        try:
            choice_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            file_dialog = QFileDialog(self)
            file_dialog.setNameFilters(["Text files (*.txt)"])
            file_dialog.selectNameFilter("Text files (*.txt)")
            file_dialog.setOption(QFileDialog.DontUseNativeDialog)
            file_dialog.exec_()
            files = file_dialog.selectedFiles()
            if files:
                filename = file_dialog.selectedFiles()[0]
                reader = AikenReader()
                self.quiz = reader.read_from_file(filename)

                for i, question in enumerate(self.quiz.questions):
                    q_item = QTreeWidgetItem(self.quizView)
                    q_item.setText(0, str(i+1))
                    q_item.setText(1, question.text)
                    for j,choice in enumerate(question.choices):
                        c_item = QTreeWidgetItem(q_item)
                        c_item.setText(0, choice_letters[j])
                        c_item.setText(1, choice.text)
                        if choice.correct:
                            c_item.setBackgroundColor(0,QColor("green"))
                            c_item.setBackgroundColor(1,QColor("green"))
                        else:
                            c_item.setBackgroundColor(0,QColor("red"))
                            c_item.setBackgroundColor(1,QColor("red"))
                        q_item.addChild(c_item)
        except Exception as err:
            box = QMessageBox()
            box.setWindowTitle("Error")
            box.setText(str(err))
            box.exec_()


    def export(self):
        try:
            if self.quiz is None:
                return
            file_dialog = QFileDialog(self)
            file_dialog.setNameFilters(["Moodle XML files (*.xml)"])
            file_dialog.selectNameFilter("Moodle XML files (*.xml)")
            file_dialog.setOption(QFileDialog.DontUseNativeDialog)
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_dialog.exec_()
            files = file_dialog.selectedFiles()
            if files:
                filename = files[0]
                saver = XMLSaver(settings=self.generateSettings())
                saver.save(self.quiz, filename)
        except Exception as err:
            box = QMessageBox()
            box.setWindowTitle("Error")
            box.setText(str(err))
            box.exec_()

    def preview(self):
        text = "What is the output of the Python code given below?\\nThis line is to demonstrate wrapping of very long lines. \"Text width\" property is used determine the text length to be wrapped.\\n`python`def mystery(n):\\n\\tif n<2:\\n\\t\\treturn 1\\n\\treturn n*mystery(n-1)\\n\\nmystery(6)\\n`\\nPlease choose an appropriate font if you are using Unicode characters."
        settings = self.generateSettings()
        ic = ImageCreator(settings=settings)
        image = ic.image(text)
        image.show()

    def fill_fonts(self):
        fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None,fontext="ttf")
        self.settingsFontName.insertItems(0, sorted(fonts))
        self.settingsFontName.insertItems(0, self.get_local_fonts())
        self.settingsFontName.setCurrentIndex(0)

    def get_local_fonts(self):
        files = []
        for dirpath, _, filenames in os.walk("./fonts/"):
            for filename in filenames:
                if filename.lower().endswith(".ttf"):
                    files.append(os.path.join(dirpath, filename))
        return files

    def fill_code_styles(self):
        styles = list(get_all_styles())
        self.settingsCodeStyle.insertItems(0, styles)

    def setupQTreeWidget(self):
        self.quizView.setColumnCount(2)
        self.quizView.setHeaderLabels(["Question/Choice", "Text"])


    def generateSettings(self):
        settings = Settings(
            font_name=self.settingsFontName.currentText(),
            font_size=self.settingsFontSize.value(),
            image_width=self.settingsImageWidth.value(),
            text_width=self.settingsTextWidth.value(),
            background_color=self.settingsBackgroundColor.text(),
            color=self.settingsTextColor.text(),
            line_numbers=self.settingsLineNumbers.isChecked(),
            code_style=self.settingsCodeStyle.currentText()
        )

        return settings



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())