import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QVBoxLayout, QLineEdit, QPushButton)

class Task:
    def __init__(self, title, deadline, description):
        self.title = title
        self.deadline = deadline
        self.description = description
        self.status = "not started"
        self.completion_date = None

class Assignment(Task):
    def __init__(self, title, deadline, description, importance):
        super().__init__(title, deadline, description)
        self.importance = importance

class Homework(Task):
    def __init__(self, title, deadline, description, time_taking):
        super().__init__(title, deadline, description)
        self.time_taking = time_taking

class Extracurricular(Task):
    def __init__(self, title, deadline, description, time_spent):
        super().__init__(title, deadline, description)
        self.time_spent = time_spent

    def to_get_progress(self):
        return self.time_spent

class StudyPlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.planner_label = QLabel("Study Planner", self)
        self.tasks = []
        # task that need to be done finish_notes,Finish_book,Finish_guide,Watch_a_deep_explanation_video,Do_worksheets
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Study Planner")
        self.setGeometry(450, 300, 500, 370)

        vbox = QVBoxLayout()
        vbox.addWidget(self.planner_label)

        self.task_list = QLabel("task that need to be done "
                                "1.finish_notes"
                                "2.Finish_book"
                                "3.Finish_guide"
                                "4.Watch_a_deep_explanation_video"
                                "5.Do_worksheets")
        vbox.addWidget(self.task_list)

        self.add_button = QPushButton("Add Task")
        vbox.addWidget(self.add_button)

        self.setLayout(vbox)
        self.planner_label.setAlignment(Qt.AlignCenter)
        self.planner_label.setStyleSheet("font-size: 50px;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    planner = StudyPlanner()
    planner.show()
    sys.exit(app.exec_())

