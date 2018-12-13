import datetime

import wx
import wx.adv

class InputPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self._init_controls()
        self._init_sizers()

    def _init_controls(self):
        self.datepicker = wx.adv.DatePickerCtrl(self, style=wx.adv.DP_DROPDOWN)
        self.datepicker.SetValue(wx.DateTime.Today())
        
        self.timepicker_arrive = TimePicker(self)

        self.company_cbox = wx.ComboBox(self, choices=["eso", "CREADIS"])

        self.task_description = wx.TextCtrl(self, size=(200,-1))

    def _init_sizers(self):
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.datepicker, 0, wx.ALL, 5)
        main_sizer.Add(self.timepicker_arrive, 0, wx.ALL, 5)
        main_sizer.Add(self.company_cbox, 0, wx.ALL, 5)
        main_sizer.Add(self.task_description, 0, wx.ALL, 5)
        self.SetSizerAndFit(main_sizer)


class TimePicker(wx.Panel):
    def __init__(self, parent, initial=datetime.time(8)):
        wx.Panel.__init__(self, parent, style=wx.BORDER_NONE)
        self.time = initial
        self._build()

    def _build(self):
        self.hour_field = wx.TextCtrl(self, value=self.time.strftime('%H'), size=(30, -1))
        self.minute_field = wx.TextCtrl(self, value=self.time.strftime('%M'), size=(30, -1))
        self.separator = wx.StaticText(self, label=':')

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.hour_field, 0)
        main_sizer.Add(self.separator, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        main_sizer.Add(self.minute_field, 0)
        self.SetSizerAndFit(main_sizer)
