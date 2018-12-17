from pathlib import Path
import datetime

import wx
import wx.adv

import config
from gui.Import import ImportDialog
from gui.InputPanel import InputPanel
from gui.WeekOverview import WeekOverview

class Frame(wx.Frame):
    def __init__(self):
        super(Frame, self).__init__(None, wx.ID_ANY, "TimeCapture")

        self.today = datetime.date.today()

        self.calendar_week = self.today.strftime('%W')
        self.date_string = self.today.strftime('%A, %d.%m.%y')

        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap('img/icon.png', wx.BITMAP_TYPE_PNG))
        self.SetIcon(icon)

        ticon = wx.adv.TaskBarIcon()
        ticon.SetIcon(icon)

        self.topfont = wx.Font(20, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        self._init_ctrls()
        self._init_sizers()
        self._init_events()

        self.SetSize(800, 600)
        
        self.Show()

    def _init_ctrls(self):
        self.panel = wx.Panel(self)
        self.menuBar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.fileItem = self.fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
        self.menu_sep = self.fileMenu.AppendSeparator()
        self.import_item = self.fileMenu.Append(-1, 'Import', 'Import times from CSV')
        self.menuBar.Append(self.fileMenu, '&File')
        self.menuBar.Append
        self.SetMenuBar(self.menuBar)

        self.cw_label = wx.StaticText(self.panel, label='KW' + self.calendar_week)
        self.date_label = wx.StaticText(self.panel, label=self.date_string)

        self.date_label.SetFont(self.topfont)
        self.cw_label.SetFont(self.topfont)
        # self.datepicker = wx.adv.DatePickerCtrl(self.panel, style=wx.adv.DP_DROPDOWN)
        # self.datepicker.SetValue(wx.DateTime.Today())

        self.inputpanel = InputPanel(self.panel)
        self.weekoverview = WeekOverview(self.panel)

    def _init_events(self):
        self.Bind(wx.EVT_MENU, self._on_quit, self.fileItem)
        self.Bind(wx.EVT_MENU, self._on_import, self.import_item)

    def _init_sizers(self):
        frame_sizer = wx.BoxSizer(wx.VERTICAL)
        date_sizer = wx.BoxSizer(wx.HORIZONTAL)
        date_sizer.Add(self.cw_label)
        date_sizer.AddStretchSpacer()
        date_sizer.Add(self.date_label)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(date_sizer, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.inputpanel, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.weekoverview, 1, wx.EXPAND | wx.ALL, 5)
        self.panel.SetSizerAndFit(main_sizer)
        frame_sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizerAndFit(frame_sizer)

    def _on_accel_newentry(self, event):
        new_inputpanel = InputPanel(self.panel)
        self.input_panel_sizer.Add(new_inputpanel, 1, wx.EXPAND)

    def _on_quit(self, event):
        exit()

    def _on_import(self, event):
        if config.testmode:
            pathname = 'test_data/12-2018.csv'
        else:
            home_dir = str(Path.home())
            with wx.FileDialog(None, "Import from CSV", home_dir, wildcard="CSV files (*.csv)|*.csv",
                            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fd:
                if fd.ShowModal() == wx.ID_CANCEL:
                    return

                pathname = fd.GetPath()

        with ImportDialog(self, pathname) as self.dlg:
            res = self.dlg.ShowModal()
