from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt, Slot


class GenericListModel(QAbstractListModel):
    def __init__(self, displayCallback, parent=None):
        super(GenericListModel, self).__init__(parent=parent)

        self.__displayCallback = displayCallback
        self.__items = None

    def items(self):
        return self.__items

    @Slot(list)
    def setItems(self, items):
        self.beginResetModel()
        self.__items = items
        self.endResetModel()

    def _getData(self, _row, item, role):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return self.__displayCallback(item)

        if role == Qt.UserRole:
            return item

        return None

    def data(self, index, role):
        if not index.isValid():
            return None

        row = index.row()
        if row < 0 or row >= self.rowCount():
            return None

        item = self.__items[row]
        return self._getData(row, item, role)

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0

        if self.__items is None:
            return 0

        return len(self.__items)
