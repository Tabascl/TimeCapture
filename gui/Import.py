import wx

from gui.CSVGrid import CSVTable

class ImportDialog(wx.Dialog):
    def __init__(self, parent, filepath):
        wx.Dialog.__init__(self, parent)
        self.table = CSVTable(filepath)
        self._init_controls()
        self._init_sizers()
        self._init_events()

    def _init_controls(self):
        self.time_grid = wx.grid.Grid(self, -1)
        self.time_grid.SetTable(self.table)
        self.time_grid.AutoSize()

        self.arrive_btn = wx.Button(self, label='Set Arrive')

    def _init_events(self):
        self.Bind(wx.EVT_BUTTON, self._on_set_arrive, self.arrive_btn)

    def _init_sizers(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)

        bottom_sizer.Add(self.arrive_btn, 0)
        bottom_sizer.AddStretchSpacer()
        bottom_sizer.Add(btn_sizer, 0)

        main_sizer.Add(self.time_grid, 1, wx.EXPAND)
        main_sizer.Add(bottom_sizer, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizerAndFit(main_sizer)

    def _on_set_arrive(self, event):
        topleft = self.time_grid.GetSelectionBlockTopLeft()
        bottomright = self.time_grid.GetSelectionBlockTopRight()
