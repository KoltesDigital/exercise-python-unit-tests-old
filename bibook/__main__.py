import sys

from PySide2.QtWidgets import QApplication

from bibook.applicationWidget import ApplicationWidget
from bibook.book import Book
from bibook.bookModel import BookModel

app = QApplication(sys.argv)

bookModel = BookModel(lambda book:'"'+book.title+'"  -   by '+book.author)



bookModel.setBooks([
    Book(title="Good Stories Are Told Silently",
         author="Kent Heeryou"),
    Book(title="Always Run Away From Danger",
         author="Ayvbin Surviving"),
    Book(title="In Case You Lose",
        author="Igotta Leuck")
])

mainWindow = ApplicationWidget()
mainWindow.setBookModel(bookModel)
mainWindow.show()

code = app.exec_()

del mainWindow
sys.exit(code)
