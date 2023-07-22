import sys
from PySide2 import QtWidgets, QtCore

from view.main_window import MainWindow
from view.table_model import TableModel

from model.data_manager import DataManager

class Application:

    def __init__(self):
        self.WEEK_DAYS = ["Mon.", "Tue.", "Wed.", "Thu.", "Fri.", "Sat.", "Sun."]

        self.app = QtWidgets.QApplication(sys.argv)
        
        self.data_manager = DataManager()

        self.table_model = TableModel(self)
        self.window = MainWindow(self, self.table_model)
    
    @property
    def tasks(self):
        return self.data_manager.get_all_tasks()
    
    def add_task(self, name):
        task_added_to_data = self.data_manager.add_task_name(name)

        if (task_added_to_data):
            self.table_model.dataChanged.emit()

        return task_added_to_data
    
    def delete_task(self, task_index):
        self.data_manager.delete_task(self.tasks[task_index])
        self.table_model.dataChanged.emit()
        
    def is_task_done(self, day_index, task_index):
        return self.data_manager.task_exists(self.WEEK_DAYS[day_index], self.tasks[task_index])
    
    def change_task_state(self, day_index, task_index):
        self.data_manager.toggle_task_state(self.WEEK_DAYS[day_index], self.tasks[task_index]) 
    
    def set_task_undone(self, day_index, task_index):
        self.data_manager.set_task_undone(self.WEEK_DAYS[day_index], self.tasks[task_index])

    def run(self):
        self.window.show()

        return self.app.exec_()
