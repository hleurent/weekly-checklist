from PySide2 import QtWidgets
from view.weeks_view import WeeksView
from view.tasks_view import TasksView
from view.table_view import TableView

class MainWindow(QtWidgets.QDialog):

    def __init__(self, application, table_model, parent = None):
        QtWidgets.QDialog.__init__(self,parent)

        self.application = application
        self.table_model = table_model

        self.setWindowTitle("Weekly Checklist App")
        self.setMinimumSize(500, 300)
        self.main_layout = QtWidgets.QVBoxLayout()

        #Table handler
        self.table_view = TableView(self.table_model, self)
        self.main_layout.addWidget(self.table_view)

        #Tasks handler
        self.tasks_manager_view = TasksView(self.application)
        self.main_layout.addWidget(self.tasks_manager_view)
        
        self.setLayout(self.main_layout)

