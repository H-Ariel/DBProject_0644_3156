from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QComboBox
from LineSeparators import QHLine
from DatabaseManager import DatabaseManager
from utils import create_table_widget


class RunFunctionsWidget(QWidget):
    def __init__(self, db : DatabaseManager):
        super().__init__()
        self.db = db
        layout = QVBoxLayout()
        
        # FUNCTION 1 - avg_dish_price
        func1_widget = QWidget()
        func1_layout = QVBoxLayout(func1_widget)
        avg_dish_price = db.fetch_data("SELECT * from avg_dish_price()")[0][0]
        func1_layout.addWidget(QLabel("FUNCTION 1 - avg_dish_price = %f" % avg_dish_price))

        # PROCEDURE 1 - update_all_orders_to_completed
        proc1_widget = QWidget()
        proc1_layout = QVBoxLayout(proc1_widget)
        operate_proc1_btn = QPushButton("Operate Procedure 1: update_all_orders_to_completed", clicked=self.operate_proc1)
        operate_proc1_btn.setFixedWidth(500)
        proc1_layout.addWidget(QLabel("PROCEDURE 1 - update_all_orders_to_completed"))
        proc1_layout.addWidget(operate_proc1_btn)

        # FUNCTION 2 - get_orders_by_status
        func2_widget = QWidget()
        self.func2_layout = QVBoxLayout(func2_widget)
        self.func2_layout.addWidget(QLabel("FUNCTION 2 - get_orders_by_status"))
        self.order_type_combo = QComboBox()
        self.order_type_combo.addItems(db.get_enum_values("order_status")) # ['Completed', 'Pending', 'Cancelled', 'Confirmed']
        self.order_type_combo.currentTextChanged.connect(self.operate_func2)
        self.func2_layout.addWidget(QLabel('get_orders_by_status'))
        self.func2_layout.addWidget(self.order_type_combo)
        self.func2_layout.addWidget(QLabel()) # place holder for table
        self.operate_func2()
        
        # add all elements
        layout.addWidget(func1_widget)
        layout.addWidget(QHLine())
        layout.addWidget(proc1_widget)
        layout.addWidget(QHLine())
        layout.addWidget(func2_widget)
        self.setLayout(layout)

    def operate_proc1(self):
        self.db.cursor.execute("CALL update_all_orders_to_completed()")
        self.db.conn.commit()
        QMessageBox.information(self, "success", "proc1 run successfully")

    def operate_func2(self):
        order_type = self.order_type_combo.currentText()

        self.db.cursor.execute("BEGIN")
        self.db.cursor.callproc("get_orders_by_status", [order_type])
        self.db.cursor.execute("FETCH ALL FROM get_orders_by_status")
        data = self.db.cursor.fetchall()
        self.db.cursor.execute("CLOSE get_orders_by_status")
        self.db.cursor.execute("COMMIT")

        # remove previous table and insert new one
        self.func2_layout.removeWidget(self.func2_layout.itemAt(3).widget())
        self.func2_layout.addWidget(create_table_widget(self.db.get_columns_for_table('RestOrder'), data))
