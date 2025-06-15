
from PyQt5.QtWidgets import QMessageBox
import RowDialogBase

class InsertRowDialog(RowDialogBase.RowDialogBase):
    def __init__(self, db_manager, table_name, parent=None):
        super().__init__(db_manager, table_name, f"Insert into {table_name}", "Insert", parent)
        self.btn.clicked.connect(self.insert_row)

    def insert_row(self):
        values = {col: self.inputs[col].text() for col in self.inputs}
        try:
            self.db.insert_into_table(self.table_name, values)
            QMessageBox.information(self, "Success", "Row inserted successfully")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
