# coding: utf-8

from PyQt5.QtWidgets import (QScrollArea, QWidget, QVBoxLayout,
        QLabel, QFrame, QPushButton)
from PyQt5.QtCore import Qt
from .introduction import Introduction

class MenuView(QScrollArea):

    def __init__(self, parent=None, update_func=None):
        super().__init__(parent)

        self.H1_HEIGHT = 50
        self.H2_HEIGHT = 50 
        self.SIDE_MARGIN = 5
        self.H1_FONT_SIZE = 18
        self.H2_FONT_SIZE = 18
        self.H3_FONT_SIZE = 16
        self.TEXT_FONT_SIZE = 14

        style = '''
            QPushButton:flat{
                text-align: left;
                padding: 1ex;
            }
            QPushButton:pressed{
                background-color: silver;
            }
            QPushButton:hover:!pressed{
                font: bold;
            }
            '''
        self.setStyleSheet(style)

        self.update_func = update_func

        self.inner = QWidget(self)

        self.vbox = QVBoxLayout(self.inner)
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setAlignment(Qt.AlignTop)

        topframe = QFrame()
        topframe.setStyleSheet('background-color: white')
        topframe.setFixedHeight(self.H1_HEIGHT)

        lbl_h1 = QLabel('Contents', topframe)
        fnt = lbl_h1.font()
        fnt.setPointSize(self.H1_FONT_SIZE)
        lbl_h1.setFont(fnt)
        lbl_h1.setFixedHeight(self.H1_HEIGHT)
        lbl_h1.setMargin(self.SIDE_MARGIN)

        self.vbox.addWidget(topframe)

        self.list_button = []
        self.add_button('Introduction')

        self.inner.setLayout(self.vbox)

        self.setWidget(self.inner)

    def buttonClicked(self, text):
        if self.update_func is not None:
            self.update_func(text)

    def add_button(self, text):
        if text not in self.list_button:
            self.list_button.append(text)
            btn = QPushButton('-' + text, self.inner)
            btn.setFlat(True)
            fnt = btn.font()
            fnt.setPointSize(self.TEXT_FONT_SIZE)
            btn.setFont(fnt)
            btn.clicked.connect(lambda: self.buttonClicked(text))
            self.vbox.addWidget(btn)
