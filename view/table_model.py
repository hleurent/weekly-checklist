from PySide2 import QtCore


class TableModel(QtCore.QAbstractTableModel):

    dataChanged = QtCore.Signal()

    def __init__(self, application, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)

        self.application = application

        self.dataChanged.connect(self.beginResetModel)
        self.dataChanged.connect(self.endResetModel)
    
    def rowCount(self, parent=None):
        return len(self.application.tasks)

    def columnCount(self, parent=None):
        return len(self.application.WEEK_DAYS)

    def data(self, index, role):
        if (role == QtCore.Qt.CheckStateRole):
            value = self.application.is_task_done(index.column(), index.row())
            return QtCore.Qt.Checked if value else QtCore.Qt.Unchecked
        return False
    
    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if (role == QtCore.Qt.CheckStateRole):
            self.application.change_task_state(index.column(), index.row())
            self.dataChanged.emit(index, index)
            return True 
        return None
    
    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.application.WEEK_DAYS[section]
            elif orientation == QtCore.Qt.Vertical:
                return self.application.tasks[section]

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable