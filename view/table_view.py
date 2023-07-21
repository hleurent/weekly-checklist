from PySide2 import QtWidgets, QtCore

class TableView(QtWidgets.QTableView):

    def __init__(self, model, parent=None):
        self.model = model

        QtWidgets.QTableView.__init__(self, parent)

        self.setModel(self.model)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setAlternatingRowColors(True)   

    def cell_updated(self, row, column):
        self.resizeRowToContents(row)
        self.resizeColumnToContents(column)