from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

def create_table_widget(columns, rows):
    table_widget = QTableWidget()
    table_widget.setColumnCount(len(columns))
    table_widget.setHorizontalHeaderLabels(columns)
    table_widget.setRowCount(len(rows))
    for row_index, row_data in enumerate(rows):
        for col_index, cell_data in enumerate(row_data):
            item = QTableWidgetItem(str(cell_data))
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table_widget.setItem(row_index, col_index, item)
    table_widget.resizeColumnsToContents()
    return table_widget
