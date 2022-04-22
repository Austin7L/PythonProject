import wx
import sqlite3 as sqlite
import wx.grid as gridlib

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,"",size=(900,400))

        panel = wx.Panel(self, -1)

        self.db = db
        self.cursor = self.db.conn.cursor()
        result = self.cursor.execute("create table if not exists Data (myindex INTEGER PRIMARY KEY AUTOINCREMENT,  id int,  login text, password text)");
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.grid = wx.grid.Grid(panel)
        rows = self.cursor.execute('SELECT Count(*) FROM Data')
        val = rows.fetchone()
        self.db_exists = val[0]
        self.grid.CreateGrid(15,20)
        self.grid.Scroll(0,0)
        self.LoadBtn = wx.Button(panel, -1, "Commit/Load")
        self.Bind(wx.EVT_BUTTON, self.onLoad, self.LoadBtn)

        vbox.Add(self.LoadBtn)
        vbox.Add(self.grid)
        panel.SetSizer(vbox)
        panel.Fit()

    def onLoad(self, event):
        if self.db_exists == 0:
            for i in range(10):
                id = i
                login = 'login'+str(i)
                password = 'pass'+str(i)
                self.cursor.execute("INSERT INTO Data VALUES (NULL,?,?,?);",(id, login, password))
            self.db.conn.commit()
        self.onLoadTable()

    def onLoadTable(self):
        self.grid.ClearGrid()

        metadata = self.cursor.execute('SELECT * from Data')
        labels = []
        for i in metadata.description:
            labels.append(i[0])
        labels = labels[1:]
        for i in range(len(labels)):
            self.grid.SetColLabelValue(i, labels[i])

        logins = self.cursor.execute('SELECT * from Data')
        for row in logins:
            row_num = row[0]
            cells = row[1:]
            for i in range(0,len(cells)):
                if cells[i] != None and cells[i] != "null":
                    self.grid.SetCellValue(row_num-1, i, str(cells[i]))
        self.Show()
        self.db.conn.commit()

class GetDatabase():
    def __init__(self):
        self.conn = sqlite.connect("logins.db")

if __name__ == "__main__":
    db=GetDatabase()
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()