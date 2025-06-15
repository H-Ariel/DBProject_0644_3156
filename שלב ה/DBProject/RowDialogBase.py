
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QFormLayout

class RowDialogBase(QDialog):
    def __init__(self, db_manager, table_name, title, button_text, parent=None):
        super().__init__(parent)
        self.db = db_manager
        self.table_name = table_name
        self.setWindowTitle(title)
        self.columns = self.db.get_columns_for_table(table_name)
        self.inputs = {}

        form_layout = QFormLayout()
        for i, col in enumerate(self.columns):
            line_edit = QLineEdit()
            form_layout.addRow(QLabel(col), line_edit)
            self.inputs[col] = line_edit

        self.btn = QPushButton(button_text)
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.btn)
        self.setLayout(main_layout)
