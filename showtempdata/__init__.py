from settings import Settings
import pyodbc

class ShowTempData:

    def __init__(self) -> None:
        self.settings = Settings()
        super().__init__()

    def __str__(self) -> str:
        result = self.params_print() + self.data_print()
        return result

    def conn_str(self,):
        server = self.settings.server
        database = self.settings.db
        driver = 'DRIVER={ODBC Driver 17 for SQL Server}'
        return driver + ';SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;'

    def params_print(self):
        result = ''
        conn = pyodbc.connect(self.conn_str())
        cursor = conn.cursor()
        cmd = 'select descrip, value from ' + self.settings.params_table + ';'
        cursor.execute(cmd)
        rows = cursor.fetchall()
        for row in rows:
            if row[0] is not None and row[1] is not None:
                s = row[0] + ', ' + row[1] + '\n'
            else:
                s = ''
            result = result + s
        cursor.close()
        return result

    def data_print(self):
        result = ''
        sep = ', '
        conn = pyodbc.connect(self.conn_str())
        cursor = conn.cursor()
        cmd = 'select account, qty, rate, amount, info, watercatagory_id, code_id, turnout, wellno from ' + \
              self.settings.data_table + ';'

        cursor.execute(cmd)
        rows = cursor.fetchall()
        for row in rows:
            s = self.fmt(row[0]) + sep + self.fmt(row[1]) + sep + \
                self.fmt(row[2]) + sep + self.fmt(row[3]) + sep + \
                self.fmt(row[4]) + sep + self.fmt(row[5]) + sep + \
                self.fmt(row[6]) + sep + self.fmt(row[7]) + sep + self.fmt(row[8]) + '\n'
            result = result + s
        cursor.close()
        return result

    def fmt(self, item) -> str:
        return str(item)
