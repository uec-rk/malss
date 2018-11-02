# coding: utf-8

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QFrame,
                             QVBoxLayout, QSplitter, QDesktopWidget)
from .params import Params
from .introduction import Introduction
from .type_of_task import TypeOfTask
from .set_file import SetFile
from .data_check import DataCheck
from .overfitting import Overfitting
from .analysis import Analysis
from .menuview import MenuView
from .results import Results
from .learning_curve import LearningCurve
from .error import Error


class App(QWidget):
    def __init__(self, lang='en'):
        super().__init__()

        self.params = Params(lang)
        self.initUI()

    def initUI(self):
        self.txt2func = {'はじめに': Introduction, 'Introduction': Introduction,
                         '分析タスク': TypeOfTask, 'Task': TypeOfTask,
                         '入力データ': SetFile, 'Input data': SetFile,
                         'データの確認': DataCheck, 'Data check': DataCheck,
                         '過学習': Overfitting, 'Overfitting': Overfitting,
                         'Analysis': Analysis, 'Results': Results,
                         'Learning curve': LearningCurve, 'Error': Error}

        self.setMinimumSize(1280, 720)
        self.setStyleSheet('background-color: rgb(242, 242, 242)')

        vbox = QVBoxLayout(self)
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)

        top = QFrame(self)
        top.setFrameShape(QFrame.StyledPanel)
        top.setFixedHeight(50)
        top.setStyleSheet('background-color: white')

        self.splitter = QSplitter(Qt.Horizontal, self)
        self.splitter.setHandleWidth(0)

        self.menuview = MenuView(self.splitter, self.update_content,
                                 self.params)
        self.menuview.setWidgetResizable(True)

        self.contentview = Introduction(self.splitter,
                                        self.menuview.add_button, self.params)
        self.contentview.setWidgetResizable(True)

        self.splitter.addWidget(self.menuview)
        self.splitter.addWidget(self.contentview)

        vbox.addWidget(top)
        vbox.addWidget(self.splitter)

        self.setLayout(vbox)

        # self.center()
        self.showMaximized()
        self.setWindowTitle('MALSS interactive')
        self.show()

    def center(self):
        # Get a rectangle of the main window.
        qr = self.frameGeometry()
        # Figure out the screen resolution; and from this resolution,
        # get the center point (x, y)
        cp = QDesktopWidget().availableGeometry().center()
        # Set the center of the rectangle to the center of the screen.
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def update_content(self, text):
        content = self.splitter.widget(1)
        if content is not None:
            if text in self.txt2func:
                content.hide()
                content.deleteLater()

                self.contentview =\
                    self.txt2func[text](self.splitter,
                                        self.menuview.add_button,
                                        self.params)
                self.contentview.setWidgetResizable(True)
                self.splitter.addWidget(self.contentview)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
