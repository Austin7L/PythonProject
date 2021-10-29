from typing import Container, Text
import wx
from wx.core import EVT_BUTTON, Colour, TextCtrl


class GetUserInfo(wx.Frame):
    def __init__(self, parent, title):
        super(GetUserInfo, self).__init__(parent, title = title, size = (250,150))
        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self) 
        # self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.label = wx.StaticText(self.panel, label = "HELLO", pos = (5, 10))
        self.btn = wx.Button(self.panel, label ="Click", pos = (5, 30)) 
        self.txtfield = wx.TextCtrl(self.panel, pos = (5, 60))
        self.btn.Bind(wx.EVT_BUTTON, self.Onclick)

        
        # wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25)
        # self.sizer.Add(self.label)
        # self.sizer.Add(self.btn)

        self.SetMinSize((400, 250)) 
        self.Centre() 
        self.Show(True) 

    def Onclick(self, event):
        # SET A STRING LABEL FOR BUTTON 
        self.btn.SetLabel("Clicked") 
        self.txtfield.SetLabel("HI")

ex = wx.App() 
GetUserInfo(None, 'Get User Infromation') 
ex.MainLoop()

# app = wx.App()

# frm = wx.Frame(None, title="Hello World!")
# panel = wx.Panel(frm)
# sizer = wx.BoxSizer(wx.VERTICAL)
# label = wx.StaticText(panel, label = "Hello World", pos = (100,50)) 
# label2 = wx.StaticText(panel, label = "Hello World")
# button = wx.Button(panel, label = "TEST")

# wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25)
# sizer.Add(label2)
# sizer.Add(button)
# panel.SetSizer(sizer)

# frm.Show()
# app.MainLoop()