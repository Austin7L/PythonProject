import sqlite3
import wx
import wx.grid as  gridlib
from wx.core import EVT_BUTTON, Center, Centre, Colour, TextCtrl
import cx_Oracle 
import jaydebeapi

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
        # self.grid.SetReadOnly(1,0, True)
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
        self.Centre() #畫面置中
        
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
        

        #connect db
        self.db = db
        self.cursor = self.db.conn.cursor()
        self.result = self.cursor.execute("select * from dspb02 where pb_userid = 'AUSTIN' ")
        self.val = self.cursor.fetchall()

        # for row in self.val:
        #     row_num = row[0]
        #     cells = row[1:]
        #     for i in range(0,len(cells)):
        #         if cells[i] != None and cells[i] != "null":
        #             self.grid.SetCellValue(row_num-1, i, str(cells[i]))

        # metadata = self.cursor.execute("select pb_userid from dspb02 where pb_userid = 'AUSTIN'")
        # labels = []
        # #Column Name
        # for i in metadata.description:
        #     labels.append(i[0])
        # labels = labels[1:]
        # for i in range(len(labels)):
        #     self.grid.SetColLabelValue(i, labels[i])
        
        # #Data
        # logins = self.cursor.execute("select pb_userid from dspb02 where pb_userid = 'AUSTIN' ")
        # print("HI",logins)
        # for row in logins:
        #     row_num = row[0]
        #     cells = row[1:]
        #     for i in range(0,len(cells)):
        #         if cells[i] != None and cells[i] != "null":
        #             self.grid.SetCellValue(row_num-1, i, str(cells[i]))


        # print(self.val)
        # self.db_exists = self.val[0]
        # for row in self.val:
        #     row_num = row[0]
        #     cells = row[1:]
        #     for i in range(0,len(cells)):
        #         if cells[i] != None and cells[i] != "null":
        #             self.grid.SetCellValue(row_num-1, i, str(cells[i]))
        test = self.cursor.execute("select * from dspb02 where pb_userid = 'AUSTIN' ")
        for i in self.cursor.execute("select * from dspb02 where pb_userid = 'AUSTIN'"):
            self.grid.SetCellValue(0, i, str(self.val[0][i]))
            for j in self.result[i]:
                self.grid.SetCellValue(i, j, str(self.val[i][j]))
        # self.grid.SetCellValue(0, 0, str(self.val[0][0]))
        # self.grid.SetCellValue(0, 1, str(self.val[0][1]))
        # self.grid.SetCellValue(0, 2, str(self.val[0][2]))
        # self.grid.SetCellValue(0, 3, str(self.val[0][3]))
        self.cursor.close()
        self.db.conn.close()


class GetDatabase():
    def __init__(self):
        userpwd = "dsod"
        # self.conn = cx_Oracle.connect('DSOD/dsod@10.1.1.91/vmdb01')

        # dsn = cx_Oracle.makedsn('10.1.1.91','1521',service_name='vmdb01')
        # conn = cx_Oracle.connect('DSOD', 'dsod', dsn)

        

        url = 'jdbc:oracle:thin:@10.1.1.91:1521:vmdb01'
        user = 'DSOD'
        password = 'dsod'
        dirver = 'oracle.jdbc.OracleDriver'
        jarFile = 'D:\\Austin\\00.Personal\\Python_workspace\\ojdbc6.jar'
        sqlStr = 'select * from T_ERP_MAT_IMGEXG'

        self.conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
        
        # curs = conn.cursor()
        # curs.execute(sqlStr)
        # result = curs.fetchall()
        # print(result)
        # curs.close()
        # conn.close()

# Run the program
if __name__ == "__main__":
    db=GetDatabase()
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()