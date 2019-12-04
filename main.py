from loadexcelparams import LoadExcelParams
from loadexceldata import LoadExcelData
from savedata import SaveData


def clear():
    from os import system, name, getenv

    _term = getenv('TERM')
    if _term is None:
        if name == 'nt':
            # for windows
            _ = system('cls')
        else:
            pass
    else:
        if name == 'nt':
            # for windows
            _ = system('cls')
        else:
            # for mac and linux(here, os.name is 'posix')
            _ = system('clear')


def user_input(msg, def_val) -> str:
    result = def_val
    s = '%s (%s):' % (msg, def_val)
    inp = input(s)
    if inp != '':
        result = inp
    return result

def menu() -> None:
    print('')
    print('')
    print('MiscISMP Import Application')
    print('')
    print('1 Display Settings')
    print('2 Import Data')
    print('3 Display Temp Tables')
    print('4 Process Data')
    print('5 Post')
    print('6 Display Post Results')
    print('')
    print('S Update Settings')
    print('')
    print('X Exit')
    return


def display_settings():
    from settings import Settings
    for i in range(80):
        print('-', end='')
    print('')
    print(Settings())
    print('Configuration File: %s' % Settings().config_filename() )
    for i in range(80):
        print('-', end='')
    return


def import_data():
    excel_params = LoadExcelParams()
    excel_data = LoadExcelData()

    dbsave = SaveData(data=excel_data.data, params=excel_params.data)
    dbsave.trunc_data()
    dbsave.save_params()
    dbsave.save_data()
    clear()
    print('Import Completed')
    print('')


def display_temp_tables():
    from showtempdata import ShowTempData
    tmpdata = ShowTempData()
    print(tmpdata)
    return


def process_data():
    from execstoredproc import ExecStoredProc
    e = ExecStoredProc()
    print(e.exec_process())
    return


def post_data():
    from execstoredproc import ExecStoredProc
    e = ExecStoredProc()
    e.exec_post()
    post_results()
    return


def post_results():
    from getpostresults import GetPostResults
    message = GetPostResults().text
    print(message)
    return


def update_settings():
    from settings import Settings
    s = Settings()
    s.user_update()
    return

done = False

clear()
while not done:
    menu()
    item = user_input('Selection', 'x').upper()
    if item == 'X':
        done = True
    elif item == '1':
        clear()
        display_settings()
    elif item == '2':
        import_data()
    elif item == '3':
        display_temp_tables()
    elif item == '4':
        process_data()
    elif item == '5':
        post_data()
    elif item == '6':
        post_results()
    elif item == 'S':
        update_settings()
    else:
        clear()
        print('Option ' + item + ' not available at this time.')

