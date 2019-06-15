import sys

from PySide2.QtWidgets import QApplication

from bibook.applicationWidget import ApplicationWidget

app = QApplication(sys.argv)

mainWindow = ApplicationWidget()
mainWindow.setBooks([
    {
        'title': "Quality Software Management",
        'author': "Gerald Weinberg",
    },
    {
        'title': "Building quality software",
        'author': "Robert L. Glass",
    }
])
mainWindow.show()

code = app.exec_()

del mainWindow
sys.exit(code)
