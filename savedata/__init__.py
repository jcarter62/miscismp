from settings import Settings
import pyodbc


class SaveData:

    def __init__(self, data: object, params: object) -> object:
        self.data = data
        self.params = params
        self.settings = Settings()
        super().__init__()

    def conn_str(self,):
        server = self.settings.server
        database = self.settings.db
        driver = 'DRIVER={ODBC Driver 17 for SQL Server}'
        return driver + ';SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;'

    def _truncate_table_(self, table):
        conn = pyodbc.connect(self.conn_str())
        cursor = conn.cursor()

        if table == 'params':
            tbl = self.settings.params_table
        elif table == 'data':
            tbl = self.settings.data_table

        cmd = 'truncate table ' + tbl + ';'
        cursor.execute(cmd)
        cursor.commit()
        cursor.close()
        return

    def trunc_data(self):
        self._truncate_table_('params')
        self._truncate_table_('data')
        return

    def save_data(self):
        for row in self.data:
            self.insert_data_row(row)

    def save_params(self):
        for row in self.params:
            self.insert_params_row(row)

    def insert_data_row(self, row):
        qt = "'"
        qc = "',"
        conn = pyodbc.connect(self.conn_str())
        cursor = conn.cursor()
        cmd = 'insert into ' + self.settings.data_table + ' ' +\
        '(account, qty, rate, amount, info, watercatagory_id, code_id, wellno, turnout) ' +\
        'values (' + str(row['account']) + ',' + str(row['qty']) + ',' + str(row['rate']) + ',' +\
        str(row['amount']) + ', null, null, ' + qt + row['code_id'] + qc +\
        qt + row['wellno'] + qc + qt + str(row['turnout']) + qt + ');'
        cursor.execute(cmd)
        cursor.commit()
        cursor.close()
        return

    def insert_params_row(self, row):
        qt = "'"
        qc = "',"
        conn = pyodbc.connect(self.conn_str())
        cursor = conn.cursor()
        cmd = 'insert into ' + self.settings.params_table + ' ' +\
        '(descrip, value) ' +\
        'values (' + qt + str(row['description']) + qt + ',' + qt + str(row['value']) + qt + ');'
        cursor.execute(cmd)
        cursor.commit()
        cursor.close()
        return
