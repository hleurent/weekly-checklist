from PySide2 import QtWidgets, QtCore, QtGui

class TableView(QtWidgets.QTableView):

    def __init__(self, model, parent=None):
        self.model = model

        QtWidgets.QTableView.__init__(self, parent)
        self.parent = parent

        self.setModel(self.model)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setAlternatingRowColors(True)

        self.col_header = self.horizontalHeader()
        self.col_header.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.col_header.customContextMenuRequested.connect(self.show_col_header_menu)

        self.row_header = self.verticalHeader()
        self.row_header.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.row_header.customContextMenuRequested.connect(self.show_task_header_menu)

    def show_col_header_menu(self, event):
        header = self.horizontalHeader()
        header_index = header.logicalIndexAt(event.x())

        self.menu = QtWidgets.QMenu(self)

        clean_action = QtWidgets.QAction('Clean', self)
        clean_action.triggered.connect(lambda: self.clean_checkboxes_on_column(header_index))
        self.menu.addAction(clean_action)
        
        self.menu.popup(QtGui.QCursor.pos())

    def show_task_header_menu(self,event):
        header = self.verticalHeader()
        header_index = header.logicalIndexAt(event.y())

        self.menu = QtWidgets.QMenu(self)

        clean_action = QtWidgets.QAction('Clean', self)
        clean_action.triggered.connect(lambda: self.clean_checkboxes_on_row(header_index))
        self.menu.addAction(clean_action)

        delete_task_action = QtWidgets.QAction('Delete Task', self)
        delete_task_action.triggered.connect(lambda: self.remove_whole_row(header_index))
        self.menu.addAction(delete_task_action)
        
        self.menu.popup(QtGui.QCursor.pos())

    def clean_checkboxes_on_column(self, col_index: int):
        for row_index in range(self.model.rowCount()):
            #Direct call to the model instead of passing through the app because it's still about UI and Checkboxes.
            index = self.model.index(row_index, col_index)
            self.model.setData(index, QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)

            self.parent.application.set_task_undone(col_index, row_index)
    
    def clean_checkboxes_on_row(self, row_index: int):
        for col_index in range(self.model.columnCount()):
            #Direct call to the model instead of passing through the app because it's still about UI and Checkboxes.
            index = self.model.index(row_index, col_index)
            self.model.setData(index, QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)

            self.parent.application.set_task_undone(col_index, row_index)

    def remove_whole_row(self, row_index: int):
        self.model.removeRow(row_index)
        self.parent.application.delete_task(row_index)



