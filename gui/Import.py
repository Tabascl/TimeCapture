import wx

from gui.CSVGrid import CSVTable

class ImportDialog(wx.Dialog):
    def __init__(self, parent, filepath):
        wx.Dialog.__init__(self, parent)
        self.table = CSVTable(filepath)
        self._init_controls()
        self._init_sizers()
        self._init_events()

        self.day_selection = None
        self.arrive_selection = None
        self.leave_selection = None

    def _init_controls(self):
        self.time_grid = wx.grid.Grid(self, -1)
        self.time_grid.SetTable(self.table)
        self.time_grid.AutoSize()

        for col in range(self.time_grid.GetNumberCols()):
            attr = wx.grid.GridCellAttr()
            attr.SetReadOnly(True)
            self.time_grid.SetColAttr(col, attr)

        self.day_btn = wx.Button(self, label='Set Day')
        self.arrive_btn = wx.Button(self, label='Set Arrive')
        self.leave_btn = wx.Button(self, label='Set Leave')

    def _init_events(self):
        self.Bind(wx.EVT_BUTTON, self._on_set_day, self.day_btn)
        self.Bind(wx.EVT_BUTTON, self._on_set_arrive, self.arrive_btn)
        self.Bind(wx.EVT_BUTTON, self._on_set_leave, self.leave_btn)

    def _init_sizers(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)

        bottom_sizer.Add(self.day_btn, 0)
        bottom_sizer.Add(self.arrive_btn, 0)
        bottom_sizer.Add(self.leave_btn, 0)
        bottom_sizer.AddStretchSpacer()
        bottom_sizer.Add(btn_sizer, 0)

        main_sizer.Add(self.time_grid, 1, wx.EXPAND)
        main_sizer.Add(bottom_sizer, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizerAndFit(main_sizer)

    def _on_set_day(self, event):
        if self.day_selection:
            old_selection = self.day_selection
        
        self.day_selection = self._selection_to_coords()
        self._paint_selection(old_selection, self.time_grid.GetDefaultCellBackgroundColour())
        self._paint_selection(self.day_selection, 'light blue')

    def _on_set_arrive(self, event):
        if self.arrive_selection:
            old_selection = self.day_selection
        
        self.arrive_selection = self._selection_to_coords()
        self._paint_selection(old_selection, self.time_grid.GetDefaultCellBackgroundColour())
        self._paint_selection(self.arrive_selection, wx.RED)

    def _on_set_leave(self, event):
        if self.leave_selection:
            old_selection = self.day_selection
        
        self.leave_selection = self._selection_to_coords()
        self._paint_selection(old_selection, self.time_grid.GetDefaultCellBackgroundColour())
        self._paint_selection(self.leave_selection, wx.GREEN)

    def _selection_to_coords(self):
        try:
            topleft = self.time_grid.GetSelectionBlockTopLeft()[0]
            bottomright = self.time_grid.GetSelectionBlockBottomRight()[0]
        except IndexError:
            cols = self.time_grid.GetSelectedCols()
            rows = self.time_grid.GetSelectedRows()

            if cols:
                topleft = [0, cols[0]]
                bottomright = [self.time_grid.NumberRows-1, cols[0]]
            elif rows:
                topleft = [rows[0], 0]
                bottomright = [rows[0], self.time_grid.NumberCols-1]
        
        return (topleft, bottomright)

    def _paint_selection(self, selection, color):
        topleft, bottomright = selection
        for x in range(topleft[0], bottomright[0]+1):
            for y in range(topleft[1], bottomright[1]+1):
                self.time_grid.SetCellBackgroundColour(x, y, color)

        self.time_grid.ClearSelection()
        self.time_grid.ForceRefresh()