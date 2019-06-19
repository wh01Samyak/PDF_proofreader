import wx
from wx.lib.splitter import MultiSplitterWindow
from selectable_pdf_panel import *
from imageform_pdf_panel import * 
import text_compare


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

		panelOne = selectable_PDF_Panel(vSplitter1)
		panelTwo = imageform_PDF_Panel(vSplitter1)
		vSplitter1.SplitVertically(panelOne, panelTwo)
		vSplitter1.SetSashGravity(0.5)

		downPanel = randomPanel(topSplitter, "#40b96c")
		topSplitter.SplitHorizontally(vSplitter, downPanel)
		topSplitter.SetSashGravity(0.85)
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(topSplitter, 1, wx.EXPAND)
		self.SetSizer(sizer)

class menuBr():
	
	def __init__(self):
		pass
	
	def define(self):

		menuBar =wx.MenuBar()

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
		self.exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit\tCtrl+Q')		
		fileButton.Append(self.exitItem)

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
	
		aboutItem = wx.MenuItem(helpButton, wx.ID_ANY, 'About')
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

		return menuBar
