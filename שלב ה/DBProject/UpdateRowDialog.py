from PyQt5.QtWidgets import QMessageBox
import RowDialogBase

class UpdateRowDialog(RowDialogBase.RowDialogBase):
    def __init__(self, db_manager, table_name, row_data, parent=None):
        super().__init__(db_manager, table_name, f"Update row in {table_name}", "Update", parent)
        self.row_data = row_data
        for i, col in enumerate(self.columns):
            self.inputs[col].setText(row_data[i])
        self.btn.clicked.connect(self.update_row)

    def update_row(self):
        values = {col: self.inputs[col].text() for col in self.columns}
        pk_col = self.columns[0]
        pk_val = self.row_data[0]
        try:
            self.db.update_row(self.table_name, pk_col, pk_val, values)
            QMessageBox.information(self, "Success", "Row updated successfully")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
