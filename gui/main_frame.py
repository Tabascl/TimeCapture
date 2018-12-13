from pathlib import Path

import wx

import config
from gui.Import import ImportDialog

class Frame(wx.Frame):
    def __init__(self):
        super(Frame, self).__init__(None, wx.ID_ANY, "Hello World")
        self._init_ctrls()
        self.Show()

    def _init_ctrls(self):
        self.menuBar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.fileItem = self.fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
        self.menu_sep = self.fileMenu.AppendSeparator()
        self.import_item = self.fileMenu.Append(-1, 'Import', 'Import times from CSV')
        self.menuBar.Append(self.fileMenu, '&File')
        self.menuBar.Append
        self.SetMenuBar(self.menuBar)
        self.Bind(wx.EVT_MENU, self._on_quit, self.fileItem)
        self.Bind(wx.EVT_MENU, self._on_import, self.import_item)

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