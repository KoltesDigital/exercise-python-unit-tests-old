# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QListWidgetItem, QWidget
from PySide2.QtCore import Qt

from bibook.ui.ApplicationWidget_ListView import Ui_ApplicationWidget
from bibook.book import Book
from bibook.bookModel import BookModel


class ApplicationWidget(QWidget):
    def __init__(self, parent=None):
        super(ApplicationWidget, self).__init__(parent=parent)

        self.__books = []
        self.__borrowedBooks = []

        # self.__bookModel = BookModel(visualisedString=lambda:title+' (from '+author+')')

        self.__ui = Ui_ApplicationWidget()
        self.__ui.setupUi(self)

        # self.__ui.bookListView.setModel(self.__bookModel)

        self.__ui.borrowBookButton.clicked.connect(self.__borrowBook)

    def setBookModel(self, bookModel):
        self.__model = bookModel
        self.__ui.bookListView.setModel(bookModel)


    def __borrowBook(self):
        index = self.__ui.bookListView.currentIndex()
        book = self.__ui.bookListView.model().data(index,Qt.UserRole)
        if book is not None:
            if book.available == True:
                self.__model.borrowBook(book)
                self.__ui.statusLabel.setText('Book Borrowed :  '+book.title)
            elif book.available == False:
                self.__model.retrieveBook(book)
                self.__ui.statusLabel.setText('Book Retrieved :  ' + book.title)