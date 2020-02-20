from PySide2.QtGui import QColor


class Book ():
    author: str
    title: str
    borrowed: bool = False
    color: QColor = QColor.fromRgb(100,100,100)