import argparse

import wx

import config
from gui.main_frame import Frame

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", help="Enable test mode",
                    action='store_true')
args = parser.parse_args()

config.testmode = args.test

if __name__ == '__main__':
    app = wx.App(redirect=True, filename='TimeCapture.log')
    Frame()
    app.MainLoop()
