from data.CSVReader import CSVReader
from wx.grid import GridTableBase

class CSVTable(GridTableBase):
    def __init__(self, filepath):
        GridTableBase.__init__(self)
        self._load_file(filepath)

    def _load_file(self, path):
        try:
            rows = CSVReader.read(path)
        except FileNotFoundError as e:
            print("Could not open file!", e)
            self.data = ['Error', 'Error']
            self.header_row = 'Error'
            return

        self.data = []
        for row in rows:
            self.data.append(row)

        self.header_row = self.data[0]
        self.data = self.data[1:]

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0])

    def GetValue(self, row, col):
        return self.data[row][col]

    def SetValue(self, row, col, value):
        self.data[row][col] = value

    def GetColLabelValue(self, col):
        return self.header_row[col]
