import os
import json


class Settings:

    def __str__(self) -> str:
        s = 'input: ' + self.input + '\n' +\
            'server:' + self.server + '\n' +\
            'db:' + self.db + '\n' +\
            'params table:' + self.params_table + '\n' +\
            'data table:' + self.data_table + '\n' +\
            'stored procedure:' + self.sp + '\n'
        return s

    def __init__(self) -> None:
        self.input = ''
        self.server = ''
        self.db = ''
        self.params_table = ''
        self.data_table = ''
        self.sp = ''

        self.load_config()
        super().__init__()

    def config_filename(self) -> str:
        appname = 'miscismp'
        osname = os.name
        if osname == 'win':
            _data_folder = os.path.join(os.getenv('APPDATA'), appname)
        else:
            _data_folder = os.path.join(os.getenv('HOME'), '.' + appname )

        if not os.path.exists(_data_folder):
            os.makedirs(_data_folder)

        filename = os.path.join(_data_folder, 'settings.json')
        return filename

    def initial_settings(self) -> object:
        result = {
            "inputfile": "data.xlsx",
            "sqlserver": "sql-svr\\mssqlr2",
            "database": "wmis_ibm",
            "params_table": "TMiscParams",
            "data_table": "TMiscData",
            "stored_proc": "sp_TMiscTransactions"
        }
        return result

    def load_config(self):
        filename = self.config_filename()

        try:
            with open(filename, 'r') as f:
                sobj = json.load(f)
        except Exception  as e:
            sobj = self.initial_settings()
            self.save_config(sobj)

        self.input = sobj['inputfile']
        self.server = sobj['sqlserver']
        self.db = sobj['database']
        self.params_table = sobj['params_table']
        self.data_table = sobj['data_table']
        self.sp = sobj['stored_proc']
        return

    def save_config(self, obj):
        filename = self.config_filename()
        with open(filename, 'w') as output:
            json.dump(obj, output)
        return

    def user_input(self, msg, def_val) -> str:
        result = def_val
        s = '%s (%s):' % (msg, def_val)
        inp = input(s)
        if inp != '':
            result = inp
        return result

    def user_update(self):
        print('')
        i_input = self.user_input('Input File', self.input)
        i_server = self.user_input('SQL Server', self.server)
        i_db = self.user_input('Database', self.db)
        i_data_table = self.user_input('Data Table', self.data_table)
        i_params_table = self.user_input('Parameter Table', self.params_table)
        i_sp = self.user_input('Stored Procedure', self.sp)
        obj = {
            "inputfile": i_input,
            "sqlserver": i_server,
            "database": i_db,
            "params_table": i_params_table,
            "data_table": i_data_table,
            "stored_proc": i_sp
        }
        self.save_config(obj=obj)
