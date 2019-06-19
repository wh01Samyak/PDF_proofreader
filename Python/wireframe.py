import wx
from gui import *

class windowClass(wx.Frame):

	def __init__(self, *args, **kwargs):
		
		super(windowClass, self).__init__(*args, **kwargs)
		self.basicGUI()

	def basicGUI(self):

		panel = mainPanel(self)

		menuBar = menuBr()
		menuBarDef = menuBar.define()
		self.Bind(wx.EVT_MENU, self.Quit, menuBar.exitItem)

		self.SetMenuBar(menuBarDef)
		self.Size=(1100,700)
		self.Centre()
		self.SetTitle('PDF Compare Tool')
		self.Show(True)

	def Quit(self,e):
		self.Close()



if __name__ == "__main__":

	app = wx.App()
	windowClass(None)
	app.MainLoop()
