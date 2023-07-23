from PySide2 import QtWidgets
from view.custom_widgets import QVLine

class WeeksView(QtWidgets.QWidget):

    def __init__(self, application, parent = None):
        QtWidgets.QWidget.__init__(self, parent)

        self.application = application
        
        self.weeks_layout = QtWidgets.QHBoxLayout()

        self.current_week_label = QtWidgets.QLabel("Current Week")
        self.weeks_layout.addWidget(self.current_week_label)

        self.all_weeks = QtWidgets.QComboBox()
        self.all_weeks.clear()
        self.all_weeks.addItems(self.application.week_names)
        self.all_weeks.setCurrentText(self.application.current_week.name)
        self.all_weeks.currentIndexChanged.connect(self._on_other_week_selected)
        self.weeks_layout.addWidget(self.all_weeks)

        self.weeks_layout.addWidget(QVLine())

        self.new_week_name = QtWidgets.QLineEdit()
        self.weeks_layout.addWidget(self.new_week_name)

        self.add_week_button = QtWidgets.QPushButton("Add Week")
        self.add_week_button.clicked.connect(self._on_add_week_clicked)
        self.weeks_layout.addWidget(self.add_week_button)

        self.setLayout(self.weeks_layout)

    def _on_add_week_clicked(self):
        new_week_name = self.new_week_name.text()

        week_added = self.application.add_week(new_week_name)

        if (week_added) :
            self.new_week_name.setText("")
            print(new_week_name + " added to WEEKS.")
            print("week names : {}".format(self.application.week_names))


            self.all_weeks.addItem(new_week_name)
            self.all_weeks.setCurrentText(new_week_name)
        
        else :
            print (new_week_name + " could not be added to WEEKS.")

    def _on_other_week_selected(self):
        self.application.change_current_week(self.all_weeks.currentText())