import wx

app = wx.App()
win = wx.Frame(None, title="Simple Editor", size=(800, 500))
loadButton = wx.Button(win, label="open", pos=(580, 5), size=(80, 25))
saveButton = wx.Button(win, label="Save", pos=(680, 5), size=(80, 25))
filename = wx.TextCtrl(win, pos=(5, 5), size=(570, 25))
contents = wx.TextCtrl(win, pos=(5, 35), size=(790, 460), style=wx.TE_MULTILINE | wx.HSCROLL)

def hello():
    print 'Hello, world!'
def openEditor():
    loadButton.Bind(wx.EVT_BUTTON,hello)
    win.Show()
    app.MainLoop()
