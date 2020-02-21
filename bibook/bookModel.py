from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex
from PySide2.QtGui import QBrush, QColor

class BookModel (QAbstractListModel):

    def __init__(self, visualisedString, available=True, parent=None):
        # ---------------
        super(BookModel, self).__init__(parent=parent)
        # ---------------
        self.__visualisedString = visualisedString
        self.__books = []



    def setBooks(self, bookList):
        # ---------------
        self.beginResetModel()
        self.__books = bookList
        self.endResetModel()


    def appendBook(self, bookUnit):
        # ---------------
        self.beginResetModel()
        if not bookUnit in self.__books:
            self.__books.append(bookUnit)
        self.endResetModel()


    def removeBook(self, bookUnit):
        # ---------------
        self.beginResetModel()
        if bookUnit in self.__books:
            self.__books.remove(bookUnit)
        self.endResetModel()


    def borrowBook(self, book):
        # ---------------
        self.beginResetModel()
        book.color = book.colorBorrowed
        book.available = False
        self.endResetModel()

    def retrieveBook(self, book):
        # ---------------
        self.beginResetModel()
        book.color = book.colorAvailable
        book.available = True
        self.endResetModel()





    def _getData(self, _row, book, role):
        # ---------------
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return self.__visualisedString(book)
        if role == Qt.UserRole:
            return book
        if role == Qt.ForegroundRole:
            return QBrush(book.color)
        return None




    def data(self, index, role):
        # ---------------
        if not index.isValid():
            return None
        row = index.row()
        if row < 0 or row >= self.rowCount():
            return None
        book = self.__books[row]
        return self._getData(row, book, role)



    def rowCount(self, parent=QModelIndex()):
        # ---------------
        if parent.isValid():
            return 0
        if not self.__books:
            return 0
        return len(self.__books)