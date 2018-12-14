import wx
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin

class DayListCtrl(wx.ListView, ListCtrlAutoWidthMixin):
    def __init__(self, parent, *args, **kwargs):
        wx.ListView.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT)
        ListCtrlAutoWidthMixin.__init__(self)
