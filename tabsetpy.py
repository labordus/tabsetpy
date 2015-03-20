import wx
# import GUI
import db
import tabsetpy_maingui
# from wsp_maingui import dlgVoorbeeld


class tspFrame(tabsetpy_maingui.Mainframe):
    # constructor

    def __init__(self, parent):
        # initialize parent class
        tabsetpy_maingui.Mainframe.__init__(self, parent)

        if db.Initialize_db() is False:
            app.Exit()

app = wx.App(False)

frame = tspFrame(None)
frame.Show(True)
app.MainLoop()
