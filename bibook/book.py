from dataclasses import dataclass, field

from PySide2.QtGui import QColor


@dataclass
class Book:
    title: str
    author: str
    available: bool = True
    color: QColor = QColor.fromRgb(40,40,40)
    colorAvailable: QColor = QColor.fromRgb(40, 40, 40)
    colorBorrowed: QColor = QColor.fromRgb(150, 150, 150)


'''
class Book ():
    def __init__(self, title, author, available, color):
        self.title = title
        self.author = author
        self.available = available
        self.color = color
'''