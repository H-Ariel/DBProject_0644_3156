from PyQt5.QtWidgets import (QStackedWidget, QWidget, QVBoxLayout, QHBoxLayout, QApplication,
                             QLabel, QPushButton, QMessageBox, QTabWidget, QInputDialog)
from PyQt5.QtCore import Qt
import sys
from DatabaseManager import DatabaseManager
from RunFunctionsWidget import RunFunctionsWidget
from RunQueriesWidget import RunQueriesWidget
from InsertRowDialog import InsertRowDialog
from UpdateRowDialog import UpdateRowDialog
from utils import create_table_widget

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager()

        self.setStyleSheet("""
            QLabel {
                font: 'SF Pro Display';
                font-size: 12pt;
            }
                           
            QPushButton {
                padding: 6px 12px;
                font-size: 11pt;
                background-color: #e1e8f0;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #c9d6e3;
            }
            QPushButton:pressed {
                background-color: #b0c4d4;
            }

            QComboBox {
                padding: 6px 12px;
                font-size: 11pt;
                background-color: #e1e8f0;
                border: none;
                border-radius: 8px;
            }
            QComboBox:hover {
                background-color: #c9d6e3;
            }
            QComboBox:pressed {
                background-color: #b0c4d4;
            }

            QTableWidget {
                background-color: #e0f7fa;
                gridline-color: gray;
                font-size: 11pt;
            }
            QHeaderView::section {
                background-color: #0288d1;
                color: white;
                padding: 4px;
                font-weight: bold;
            }
        """)

        self.setWindowTitle("Space Colonies Management System")
        self.resize(1200, 800)

        title = QLabel("🪐 Space Colonies Management System")
        title.setStyleSheet("font-size: 20pt; font-weight: bold; margin: 10px;")
        title.setAlignment(Qt.AlignCenter)

        self.main_layout = QHBoxLayout()
        
        self.view_tables_button = QPushButton("View All Tables", clicked=self.show_tables)
        self.tables_view = QTabWidget()
        self.refresh_tables()

        self.run_func_widget = RunFunctionsWidget(self.db_manager)
        self.run_func_widget_button = QPushButton("Run Functions & Procedures", clicked=self.show_run_func_widget)

        self.run_queries_widget = RunQueriesWidget(self.db_manager)
        self.run_queries_widget_button = QPushButton("Run Queries", clicked=self.show_run_queries_widget)

        sidebar_widget = QWidget()
        sidebar_widget.setStyleSheet("border-right: 1px solid gray; padding-right: 10px;")
        self.sidebar_layout = QVBoxLayout(sidebar_widget)
        self.sidebar_layout.addWidget(self.view_tables_button)
        self.sidebar_layout.addWidget(self.run_func_widget_button)
        self.sidebar_layout.addWidget(self.run_queries_widget_button)
        self.sidebar_layout.setSpacing(10)
        self.sidebar_layout.addStretch()

        self.content_stack = QStackedWidget()
        self.content_stack.addWidget(self.tables_view)
        self.content_stack.addWidget(self.run_func_widget)
        self.content_stack.addWidget(self.run_queries_widget)
        self.content_stack.setCurrentWidget(self.tables_view)

        self.main_layout.addWidget(sidebar_widget)
        self.main_layout.addWidget(self.content_stack)

        main_vbox = QVBoxLayout()
        main_vbox.addWidget(title)
        main_vbox.addLayout(self.main_layout)
        self.setLayout(main_vbox)

    def show_tables             (self): self.content_stack.setCurrentWidget(self.tables_view)
    def show_run_func_widget    (self): self.content_stack.setCurrentWidget(self.run_func_widget)
    def show_run_queries_widget (self): self.content_stack.setCurrentWidget(self.run_queries_widget)

    def refresh_tables(self):
        self.tables_view.clear()
        tables_data = self.db_manager.get_all_tables()
        if isinstance(tables_data, str):
            QMessageBox.critical(self, "Error", tables_data)
            return
        
        for table_name, data in tables_data.items():
            table_widget = create_table_widget(data["columns"], data["rows"])

            insert_button = QPushButton(f"Insert into {table_name}", clicked=lambda _, t=table_name: self.open_insert_dialog(t))
            insert_button.setFixedWidth(300)
            update_button = QPushButton(f"Update row in {table_name}", clicked=lambda _, t=table_name, w=table_widget: self.open_update_dialog(t, w))
            update_button.setFixedWidth(300)
            if table_name in ['colony', 'crew', 'equipment', 'infrastructure', 'mission', 'researcher']:
                delete_button = QPushButton(f"Delete row in {table_name}", clicked=lambda _, t=table_name: self.open_delete_dialog(t))
                delete_button.setFixedWidth(300)
            else:
                delete_button = None

            btns_container = QWidget()
            btns_layout = QHBoxLayout(btns_container)
            btns_layout.addWidget(insert_button)
            btns_layout.addWidget(update_button)
            if delete_button: btns_layout.addWidget(delete_button)
            btns_layout.setAlignment(Qt.AlignLeft)
            tab_container = QWidget()
            tab_layout = QVBoxLayout(tab_container)
            tab_layout.addWidget(btns_container)
            tab_layout.addWidget(table_widget)
            self.tables_view.addTab(tab_container, table_name)
    
    def open_insert_dialog(self, table_name):
        dialog = InsertRowDialog(self.db_manager, table_name, self)
        if dialog.exec_():
            self.refresh_tables()

    def open_update_dialog(self, table_name, table_widget):
        row, ok = QInputDialog.getInt(self, "Update Row", "Row number:")
        if ok:
            row -= 1
            if row < 0 or row >= table_widget.rowCount():
                QMessageBox.critical(self, 'Error', 'Invalid row number!')
                return

            row_data = [table_widget.item(row, col).text() if table_widget.item(row, col) else "" 
                        for col in range(table_widget.columnCount())]
            dialog = UpdateRowDialog(self.db_manager, table_name, row_data, self)
            if dialog.exec_():
                self.refresh_tables()
    
    def open_delete_dialog(self, table_name):
        row_id, ok = QInputDialog.getInt(self, "Delete Row", f"{table_name.title()} id:")
        if ok:
            try:
                self.db_manager.delete_row(table_name, f'T WHERE T.{table_name}_id = {row_id};')
                QMessageBox.information(self, "Success", "Row deleted successfully")
                self.refresh_tables()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    main_window.move(QApplication.primaryScreen().availableGeometry().center() - main_window.rect().center())  # move app to screen's center
    sys.exit(app.exec_())
