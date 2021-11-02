import wx
import wx.grid as  gridlib
from wx.core import EVT_BUTTON, Colour, TextCtrl

class MyForm(wx.Frame):
    name = ""
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Grid with Popup Menu")
 
        # Add a panel so it looks the correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.label = wx.StaticText(self.panel, label = "姓名：")
        self.btn = wx.Button(self.panel, label ="Search", pos = (5, 30)) 
        self.txtfield = wx.TextCtrl(self.panel, pos = (5, 60))
        self.btn.Bind(wx.EVT_BUTTON, self.Onclick)
        self.grid = gridlib.Grid(self.panel)
        self.grid.SetReadOnly()
        self.grid.CreateGrid(25,8)
        self.grid.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK,
                       self.showPopupMenu)
        
        v_sizer = wx.BoxSizer(wx.VERTICAL)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        h_sizer.Add(self.label, proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
        h_sizer.Add(self.txtfield, proportion=0,flag=wx.EXPAND|wx.ALL,border=0)

        v_sizer.Add(self.btn)
        v_sizer.Add(self.grid, 1, wx.EXPAND, 5)

        sizer_all = wx.BoxSizer(wx.VERTICAL)
        sizer_all.Add(h_sizer, proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
        sizer_all.Add(v_sizer, proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
        self.panel.SetSizer(sizer_all)
        
    #----------------------------------------------------------------------
    def showPopupMenu(self, event):
        """
        Create and display a popup menu on right-click event
        """
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()
            self.popupID3 = wx.NewId()
            # make a menu
        
        menu = wx.Menu()
        # Show how to put an icon in the menu
        item = wx.MenuItem(menu, self.popupID1,"One")
        menu.AppendItem(item)
        menu.Append(self.popupID2, "Two")
        menu.Append(self.popupID3, "Three")
        
        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()

    def Onclick(self, event):
        # SET A STRING LABEL FOR BUTTON 
        # self.btn.SetLabel("Clicked") 
        # self.txtfield.SetLabel("HI")
        name = self.txtfield.GetValue()
        self.grid.SetCellValue(0, 0, name)


# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()