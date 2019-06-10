import wx
from wx.lib.splitter import MultiSplitterWindow

class PDF_Panel(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		self.SetBackgroundColour('#b95540')

		button = wx.Button(self, id = wx.ID_ANY, label = "Add Document")
		button.Bind(wx.EVT_BUTTON, self.onButton)

	def onButton(self, event):
		print("Button pressed!")
		wild = "*.pdf;*.xps;*.oxps;*.epub;*.cbz;*.fb2"
		dlg = wx.FileDialog(None, message = "Choose a file to display", wildcard = wild, style=wx.FD_OPEN|wx.FD_CHANGE_DIR)
		if dlg.ShowModal() == wx.ID_OK:
			filename = dlg.GetPath()
		else:
			filename = None
		dlg.Destroy()
		if filename:
			dlg = PDFdisplay(None, filename)
			rc = dlg.ShowModal()


class randomPanel(wx.Panel):

	def __init__(self, parent, color):
		wx.Panel.__init__(self, parent)
		self.SetBackgroundColour(color)


class mainPanel(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		topSplitter = wx.SplitterWindow(self)
		vSplitter = wx.SplitterWindow(topSplitter) 
		vSplitter1 = wx.SplitterWindow(vSplitter)

		errorLogPanel = randomPanel(vSplitter, "#40b96c")
		vSplitter.SplitVertically(vSplitter1, errorLogPanel)
		vSplitter.SetSashGravity(0.85)

		panelOne = PDF_Panel(vSplitter1)
		panelTwo = PDF_Panel(vSplitter1)
		vSplitter1.SplitVertically(panelOne, panelTwo)
		vSplitter1.SetSashGravity(0.5)

		downPanel = randomPanel(topSplitter, "#40b96c")
		topSplitter.SplitHorizontally(vSplitter, downPanel)
		topSplitter.SetSashGravity(0.85)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(topSplitter, 1, wx.EXPAND)
		self.SetSizer(sizer)
		

class windowClass(wx.Frame):

	def __init__(self, *args, **kwargs):
		
		super(windowClass, self).__init__(*args, **kwargs)
		self.basicGUI()

	def basicGUI(self):

		panel = mainPanel(self)

		menuBar = wx.MenuBar()

		fileButton = wx.Menu()
		editButton = wx.Menu()
		viewButton = wx.Menu()
		compareButton = wx.Menu()
		helpButton = wx.Menu()

		newItem = wx.MenuItem(fileButton, wx.ID_ANY, 'New')
		fileButton.Append(newItem)
		openItem = wx.MenuItem(fileButton, wx.ID_ANY, 'Open')
		fileButton.Append(openItem)
		saveItem = wx.MenuItem(fileButton, wx.ID_ANY, 'Save')
		fileButton.Append(saveItem)
		saveAsItem = wx.MenuItem(fileButton, wx.ID_ANY, 'Save As')
		fileButton.Append(saveAsItem)
		closeDocumentItem = wx.MenuItem(fileButton, wx.ID_ANY, 'Close Document')
		fileButton.Append(closeDocumentItem)
		exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit\tCtrl+Q')		
		fileButton.Append(exitItem)

		undoItem = wx.MenuItem(editButton, wx.ID_ANY, 'Undo')
		editButton.Append(undoItem)
		redoItem = wx.MenuItem(editButton, wx.ID_ANY, 'Redo')
		editButton.Append(redoItem)
		copyDifferenceItem = wx.MenuItem(editButton, wx.ID_ANY, 'Copy Difference')
		editButton.Append(copyDifferenceItem)
		ignoreDifferenceItem = wx.MenuItem(editButton, wx.ID_ANY, 'Ignore Difference')
		editButton.Append(ignoreDifferenceItem)
		selectAllDifferenceItem = wx.MenuItem(editButton, wx.ID_ANY, 'Select All Difference')
		editButton.Append(selectAllDifferenceItem)

		splitItem = wx.MenuItem(viewButton, wx.ID_ANY, 'Split Horizontally/Vertically')
		viewButton.Append(splitItem)
		syncronizeScrollingItem = wx.MenuItem(viewButton, wx.ID_ANY, 'Syncronize Scrolling')
		viewButton.Append(syncronizeScrollingItem)
		zoomInItem = wx.MenuItem(viewButton, wx.ID_ANY, 'Zoom In')
		viewButton.Append(zoomInItem)
		zoomOutItem = wx.MenuItem(viewButton, wx.ID_ANY, 'Zoom Out')
		viewButton.Append(zoomOutItem)
		fitToWidthItem = wx.MenuItem(viewButton, wx.ID_ANY, 'Fit to Width')
		viewButton.Append(fitToWidthItem)
		nextPageItem = wx.MenuItem(viewButton, wx.ID_ANY, 'Next Page')
		viewButton.Append(nextPageItem)
		previousPageItem = wx.MenuItem(viewButton, wx.ID_ANY, 'Previous Page')
		viewButton.Append(previousPageItem)

		compareDocumentItem = wx.MenuItem(compareButton, wx.ID_ANY, 'Compare Documents')
		compareButton.Append(compareDocumentItem)
		nextDifferenceItem = wx.MenuItem(compareButton, wx.ID_ANY, 'Next Difference')
		compareButton.Append(nextDifferenceItem)
		previousDifferenceItem = wx.MenuItem(compareButton, wx.ID_ANY, 'Previous Difference')
		compareButton.Append(previousDifferenceItem)
		languageItem = wx.Menu()
		advancedItem = wx.Menu()
		compareButton.AppendSubMenu(languageItem,'Language')
		compareButton.AppendSubMenu(advancedItem, 'Advanced')
	
		aboutItem = wx.MenuItem(helpButton, wx.ID_ANY, 'Adout')
		helpButton.Append(aboutItem)	

		languageItem.Append(wx.ID_ANY,'English')	
		languageItem.Append(wx.ID_ANY,'Hindi')

		advancedItem.Append(wx.ID_ANY,'Find difference in punctuation')
		advancedItem.Append(wx.ID_ANY,'Find one-letter difference')


		menuBar.Append(fileButton, 'File')
		menuBar.Append(editButton, 'Edit')
		menuBar.Append(viewButton, 'View')
		menuBar.Append(compareButton, 'Compare')
		menuBar.Append(helpButton, 'Help')

		self.Bind(wx.EVT_MENU, self.Quit, exitItem)

		self.SetMenuBar(menuBar)
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
