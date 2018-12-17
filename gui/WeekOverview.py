import wx
from wx.dataview import DataViewListCtrl

class WeekOverview(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.dayrow = ['Montag', '', '', '']
        self.data = ['Creadis', 'HOURS', '9.5h', 'Viel Arbeit']
        
        self._init_controls()
        self._init_sizers()
        self._init_events()

    def _init_controls(self):
        self.listctrl = DataViewListCtrl(self, style=wx.dataview.DV_HORIZ_RULES)

        self.listctrl.AppendTextColumn('Company')
        self.listctrl.AppendTextColumn('Task')
        self.listctrl.AppendTextColumn('Hours')
        self.listctrl.AppendTextColumn('Description')

        self.listctrl.AppendItem(self.dayrow)
        self.listctrl.AppendItem(self.data)

    def _init_sizers(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.listctrl, 1, wx.EXPAND)
        self.SetSizerAndFit(main_sizer)

    def _init_events(self):
        self.Bind(wx.EVT_SIZE, self._on_resize_list, self)

    def _on_resize_list(self, event):
        event.Skip()
        new_width = self.GetSize()[0]
        cur_width = 0

        for i in range(4):
            col = self.listctrl.GetColumn(i)
            cur_width += col.GetWidth()
            
            if i == 3:
                last_col_width = col.GetWidth()

        diff = new_width - cur_width
        set_width = last_col_width + diff - 4
        if set_width > 0:
            self.listctrl.GetColumn(3).SetWidth(set_width)

