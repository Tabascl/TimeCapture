import wx

from gui.CSVGrid import CSVTable

class ImportDialog(wx.Dialog):
    def __init__(self, parent, filepath):
        wx.Dialog.__init__(self, parent)
        self.table = CSVTable(filepath)
        self._init_controls()
        self._init_sizers()

    def _init_controls(self):
        self.time_grid = wx.grid.Grid(self, -1)
        self.time_grid.SetTable(self.table)
        self.time_grid.AutoSize()
    
    def _init_sizers(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.time_grid, 1, wx.EXPAND)

        self.SetSizerAndFit(main_sizer)
