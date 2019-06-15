# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QListWidgetItem, QWidget

from bibook.ui.ApplicationWidget_ListWidget import Ui_ApplicationWidget


class ApplicationWidget(QWidget):
    def __init__(self, parent=None):
        super(ApplicationWidget, self).__init__(parent=parent)

        self.__books = None
        self.__borrowedBooks = []

        self.__ui = Ui_ApplicationWidget()
        self.__ui.setupUi(self)

        self.__ui.borrowBookButton.clicked.connect(self.__borrowBook)

    def setBooks(self, books):
        self.__books = books
        for book in books:
            QListWidgetItem(book['title'] + ", by " + book['author'], self.__ui.bookListWidget)

    def __borrowBook(self):
        row = self.__ui.bookListWidget.currentRow()
        if row >= 0:
            book = self.__books[row]

            self.__borrowedBooks.append(book)

            self.__ui.statusLabel.setText(u"Book \"" + book['title'] + u"\" borrowed!")
