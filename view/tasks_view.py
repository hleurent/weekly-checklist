from PySide2 import QtWidgets

class TasksView(QtWidgets.QWidget):

    def __init__(self, application, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.application = application

        self.new_task_layout = QtWidgets.QHBoxLayout()

        self.new_task_label = QtWidgets.QLabel("New Task : ")
        self.new_task_layout.addWidget(self.new_task_label)

        self.new_task_name = QtWidgets.QLineEdit()
        self.new_task_layout.addWidget(self.new_task_name)

        self.add_task_button = QtWidgets.QPushButton("Add Task")
        self.add_task_button.clicked.connect(self._on_task_button_clicked)
        self.new_task_layout.addWidget(self.add_task_button)

        self.setLayout(self.new_task_layout)
    
    def _on_task_button_clicked(self):
        new_task_name = self.new_task_name.text()

        task_added = self.application.add_task(new_task_name)

        if (task_added) :
            self.new_task_name.setText("")
            print(new_task_name + " added to tasks list.")
        
        else :
            print (new_task_name + " could not be added to tasks list.")