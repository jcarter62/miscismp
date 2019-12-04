from settings import Settings
from openpyxl import load_workbook


class LoadExcelParams:

    def __init__(self) -> None:
        self.input_file = Settings().input
        self.data = []
        self.load_params()
        super().__init__()

    def load_params(self):
        wb = load_workbook(self.input_file)

        sheet = wb['parameters']
        rows = sheet.rows
        for r in rows:
            if (r[0].row > 1) and (r[0].value is not None):
                row = {'description': r[0].value, 'value': r[1].value }
                self.data.append(row)

