from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QTabWidget
from DatabaseManager import DatabaseManager
from utils import create_table_widget

QUERIES_FILE_PATH = './select-queries.sql'


class RunQueriesWidget(QWidget):
    def __init__(self, db : DatabaseManager):
        super().__init__()
        self.db = db

        run_btn = QPushButton("Run Queries!", clicked=self.run_queries)
        self.queris_view = QTabWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(run_btn)
        self.layout.addWidget(self.queris_view)
        self.setLayout(self.layout)

        self.run_queries()


    def run_queries(self):
        self.queris_view.clear()

        with open(QUERIES_FILE_PATH) as queries_file:
            for query in queries_file.read().split('\n\n'):
                try:
                    data = self.db.fetch_data_with_columns(query)
                except Exception as e:
                    QMessageBox.critical(self, "Query Error", str(e))
                    continue

                query_title = query.split('\n')[0][3:]
                vbox = QVBoxLayout()
                vbox.addWidget(QLabel(query_title))
                vbox.addWidget(create_table_widget(data['columns'], data['rows']))
                container = QWidget()
                container.setLayout(vbox)
                self.queris_view.addTab(container, query_title.split('.')[0])
