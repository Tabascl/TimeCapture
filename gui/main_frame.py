from pathlib import Path

import wx
import wx.adv

import config
from gui.Import import ImportDialog
from gui.InputPanel import InputPanel

class Frame(wx.Frame):
    def __init__(self):
        super(Frame, self).__init__(None, wx.ID_ANY, "Hello World")
        self._init_ctrls()
        self._init_sizers()
        self._init_accel()
        self._init_events()

        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap('img/icon.png', wx.BITMAP_TYPE_PNG))
        self.SetIcon(icon)

        ticon = wx.adv.TaskBarIcon()
        ticon.SetIcon(icon)

        self.Show()

    def _init_accel(self):
        self.newentry_id = wx.NewId()
        entry = wx.AcceleratorEntry()
        entry.Set(wx.ACCEL_CTRL, wx.WXK_RETURN, id=self.newentry_id)

        accel_tbl = wx.AcceleratorTable([entry])
        self.SetAcceleratorTable(accel_tbl)

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

        self.date_label = wx.StaticText(self.panel, label='Date:')
        self.datepicker = wx.adv.DatePickerCtrl(self.panel, style=wx.adv.DP_DROPDOWN)
        self.datepicker.SetValue(wx.DateTime.Today())

        self.inputpanel = InputPanel(self.panel)

    def _init_events(self):
        self.Bind(wx.EVT_MENU, self._on_quit, self.fileItem)
        self.Bind(wx.EVT_MENU, self._on_import, self.import_item)
        self.Bind(wx.EVT_MENU, self._on_accel_newentry, id=self.newentry_id)

    def _init_sizers(self):
        frame_sizer = wx.BoxSizer(wx.VERTICAL)
        date_sizer = wx.BoxSizer(wx.HORIZONTAL)
        date_sizer.Add(self.date_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
        date_sizer.Add(self.datepicker)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(date_sizer, 0, wx.ALL, 5)
        main_sizer.Add(self.inputpanel, 1, wx.EXPAND)
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