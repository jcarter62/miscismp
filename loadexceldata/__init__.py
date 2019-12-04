from settings import Settings
from openpyxl import load_workbook


class LoadExcelData:

    def __init__(self) -> None:
        self.input_file = Settings().input
        self.data = []
        self.load_data()
        super().__init__()

    def load_data(self):
        wb = load_workbook(self.input_file)

        sheet = wb['data']
        rows = sheet.rows
        for r in rows:
            if (r[0].row > 1) and (r[0].value is not None):
                row = {
                    'account': r[0].value, 'qty': r[1].value,
                    'rate': r[2].value, 'amount': r[3].value,
                    'turnout': r[4].value, 'code_id': r[5].value,
                    'wellno': r[6].value
                }
                self.data.append(row)
