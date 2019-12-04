from settings import Settings
import pyodbc


class ExecStoredProc:

    def __init__(self):
        self.results = ''
        self.settings = Settings()
        return

    def _conn_str_(self,):
        server = self.settings.server
        database = self.settings.db
        driver = 'DRIVER={ODBC Driver 17 for SQL Server}'
        return driver + ';SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;'

    def _execute_(self, proc, function):
        results = ''
        qt = "'"
        conn = pyodbc.connect(self._conn_str_())
        cursor = conn.cursor()

        cmd = 'exec ' + self.settings.sp + ' ' + qt + function + qt + ';'
        cursor.execute(cmd)
        try:
            rows = cursor.fetchall()
            for row in rows:
                for col in row:
                    results = results + str(col) + ', '
                results = results  + '\n'
        except Exception as e:
            results = str(e)

        cursor.commit()
        cursor.close()
        self.results = results
        return

    def exec_process(self):
        proc = self.settings.sp
        self._execute_(proc, function='createbatch')
        return self.results

    def exec_post(self):
        proc = self.settings.sp
        self._execute_(proc, function='PostBatch')
        return self.results


