import argparse

import wx
import wx.grid
from gui.CSVGrid import CSVTable
from gui.Import import ImportDialog
from pathlib import Path

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
        self.Bind(wx.EVT_MENU, self.OnQuit, self.fileItem)
        self.Bind(wx.EVT_MENU, self.OnImport, self.import_item)

    def OnQuit(self, event):
        exit()

    def OnImport(self, event):
        if args.test:
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

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", help="Enable test mode",
                    action='store_true')
args = parser.parse_args()

if __name__ == '__main__':
    app = wx.App(redirect=True, filename='TimeCapture.log')
    Frame()
    app.MainLoop()
