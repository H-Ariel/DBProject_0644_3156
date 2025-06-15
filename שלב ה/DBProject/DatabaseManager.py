import psycopg2
import json

class DatabaseManager:
    def __init__(self):
        config = json.load(open('config.json'))
        self.conn = psycopg2.connect(
            host=config['host'],
            port=config["port"],
            database=config["database"],
            user=config["username"],
            password=config["password"])
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        self.conn.close()
    
    def fetch_data(self, query : str):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def fetch_data_with_columns(self, query : str) -> dict:
        self.cursor.execute(query)
        rows = self.fetch_data(query)
        columns = [desc[0] for desc in self.cursor.description]
        return {"columns": columns, "rows": rows}

    def get_all_tables(self):
        try:
            data = self.fetch_data("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE';")
            table_names = [row[0] for row in data]
            table_data = {}
            for table in table_names:
                rows = self.fetch_data(f'SELECT * FROM "{table}"')
                columns = [desc[0] for desc in self.cursor.description]
                table_data[table] = {"columns": columns, "rows": rows}
            return table_data
        except Exception as e:
            return f"Error retrieving tables: {e}"
    
    def get_columns_for_table(self, table_name : str):
        self.cursor.execute(f'SELECT * FROM "{table_name}" LIMIT 0')
        return [desc[0] for desc in self.cursor.description]

    def insert_into_table(self, table_name : str, column_values : dict):
        try:
            columns = ', '.join(f'"{c}"' for c in column_values.keys())
            placeholders = ', '.join(['%s'] * len(column_values))
            values = list(column_values.values())
            query = f'INSERT INTO "{table_name}" ({columns}) VALUES ({placeholders})'
            self.cursor.execute(query, values)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()  # הוסף את זה כדי לשחרר טרנזקציה תקועה
            raise e
    
    def update_row(self, table_name : str, pk_col : str, pk_val, column_values : dict):
        set_clause = ', '.join(f'"{col}" = %s' for col in column_values.keys())
        values = list(column_values.values())
        query = f'UPDATE "{table_name}" SET {set_clause} WHERE "{pk_col}" = %s'
        self.cursor.execute(query, values + [pk_val])
        self.conn.commit()
    
    def delete_row(self, table_name, cond):
        query = f"DELETE FROM {table_name} {cond}"
        self.cursor.execute(query)
        self.conn.commit()

    def get_enum_values(self, enum_type):
        self.cursor.execute(f"SELECT unnest(enum_range(NULL::{enum_type}))")
        return [row[0] for row in self.cursor.fetchall()]
