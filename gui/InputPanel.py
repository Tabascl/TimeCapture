import datetime

import wx
import wx.adv

class InputPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self._init_controls()
        self._init_sizers()

    def _init_controls(self):
        self.timepicker_arrive = TimePicker(self)
        self.timepicker_leave = TimePicker(self, type_arrive=False)

        self.company_cbox = wx.ComboBox(self, choices=["eso", "CREADIS"])

        self.task_description = wx.TextCtrl(self, size=(200,-1))

    def _init_sizers(self):
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.timepicker_arrive, 0, wx.RIGHT, 5)
        main_sizer.Add(self.timepicker_leave, 0, wx.RIGHT, 5)
        main_sizer.Add(self.company_cbox, 0, wx.RIGHT, 5)
        main_sizer.Add(self.task_description, 1)
        self.SetSizerAndFit(main_sizer)


class TimePicker(wx.Panel):
    def __init__(self, parent, initial=datetime.time(8), type_arrive=True):
        wx.Panel.__init__(self, parent, style=wx.BORDER_NONE)
        self.time = initial
        self.type_arrive = type_arrive
        self._build()

    def _build(self):
        if self.type_arrive:
            path = 'img/arrow_arrive.png'
        else:
            path = 'img/arrow_leave.png'
        bmp = wx.Bitmap(path, wx.BITMAP_TYPE_PNG)
        self.arrow = wx.StaticBitmap(self, bitmap=bmp, size=(-1, 20))
        self.hour_field = wx.TextCtrl(self, value=self.time.strftime('%H'), size=(25, -1))
        self.minute_field = wx.TextCtrl(self, value=self.time.strftime('%M'), size=(25, -1))
        self.separator = wx.StaticText(self, label=':')

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.arrow, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
        main_sizer.Add(self.hour_field, 0)
        main_sizer.Add(self.separator, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        main_sizer.Add(self.minute_field, 0)
        self.SetSizerAndFit(main_sizer)
