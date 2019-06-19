import wx
from gui import *
import text_compare

class windowClass(wx.Frame):

	def __init__(self, *args, **kwargs):
		
		super(windowClass, self).__init__(*args, **kwargs)
		self.basicGUI()

	def basicGUI(self):

		panel = mainPanel(self)

		menuBar = menuBr()
		menuBarDef = menuBar.define()
		self.Bind(wx.EVT_MENU, self.Quit, menuBar.exitItem)
		self.Bind(wx.EVT_MENU, self.Compare, menuBar.compareDocumentItem)		

		self.SetMenuBar(menuBarDef)
		self.Size=(1100,700)
		self.Centre()
		self.SetTitle('PDF Compare Tool')
		self.Show(True)

	def Quit(self,e):
		self.Close()
	
	def Compare(self,e):
		if( selectableUpload() and imageformUpload() ):
			path = imageformPath()
			f1 = open(path+"/image-form.txt","r")
			text1 = f1.read()	
			f1.close()
			path = selectablePath()
			f2 = open(path+"/selectable.txt","r")
			text2 = f2.read()	
			f2.close()
			errorLog = text_compare.diff(text1,text2)
			print(errorLog)

		elif(selectableUpload()):
			wx.MessageBox('Image-form PDF not uploaded.', 'Error', wx.OK | wx.ICON_ERROR)

		elif(imageformUpload()):
			wx.MessageBox('Selectable PDF not uploaded.', 'Error', wx.OK | wx.ICON_ERROR)

		else:
			wx.MessageBox('PDFs not uploaded.', 'Error', wx.OK | wx.ICON_ERROR)


if __name__ == "__main__":

	app = wx.App()
	windowClass(None)
	app.MainLoop()
