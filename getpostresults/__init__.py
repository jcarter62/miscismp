from settings import Settings
import pyodbc


class GetPostResults:

    def __init__(self):
        self.text = ''
        self.settings = Settings()
        self._execute_()
        return

    def _conn_str_(self,):
        server = self.settings.server
        database = self.settings.db
        driver = 'DRIVER={ODBC Driver 17 for SQL Server}'
        return driver + ';SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;'

    def _execute_(self):
        results = ''
        batch_id = -1
        conn = pyodbc.connect(self._conn_str_())
        cursor = conn.cursor()

        cmd = 'select max(batchid) as batchid from batches b ' +\
            'where b.Description2 like \'%sp_TMiscTransactions%\' and b.posted = 1 '

        cursor.execute(cmd)
        try:
            row = cursor.fetchone()
            if row is None:
                results = 'Batch Not Found'
            else:
                batch_id = int(row[0])
        except Exception as e:
            results = str(e)

        if batch_id > 0:
            # We found a batch, now get the latest message.
            cmd = 'select top 1 message from batch_message bm where bm.batchid = %d order by stamp desc' % batch_id
            cursor.execute(cmd)
            try:
                row = cursor.fetchone()
                if row is None:
                    results = 'Results not available'
                else:
                    results = row[0]
            except Exception as e:
                results = str(e)

        cursor.close()
        self.text = results
        return
