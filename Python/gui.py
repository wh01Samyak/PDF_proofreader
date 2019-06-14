import wx
import wx.lib.sized_controls as sc
from wx.lib.splitter import MultiSplitterWindow
import extract_images
import os
import shutil

class Panel(wx.Panel):
    def __init__(self, parent,loc,i):
        wx.Panel.__init__(self, parent, size=(800,100))
        color='#A'+str(i)+'FF00'
        # several "Panels" sized added together 
        # are bigger than ScrolledPanel size

        self.SetMinSize( (800, 100) )
        self.SetBackgroundColour( color )

        img = wx.Image(loc+str(i)+".png", wx.BITMAP_TYPE_ANY)
        imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(img))
        imageCtrl.SetBitmap(wx.Bitmap(img))

class BigPanel(wx.Panel):
    def __init__(self, parent, loc, cnt):
        wx.Panel.__init__(self, parent, size=(800,800))

        img = []        
        for i in range(cnt):
            img.append(Panel(self,loc,i))

        sizer = wx.BoxSizer(wx.VERTICAL)

        for i in range(cnt):
            sizer.Add( img[i], 1, wx.ALL | wx.EXPAND, 15 )
        
        self.SetSizer( sizer )

class MyFileDropTarget(wx.FileDropTarget):

    def __init__(self, window,prePath):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.prePath = prePath

    def OnDropFiles(self, x, y, filenames):
        print(filenames[0])
        
        if(filenames[0][-4:] != '.pdf'):
                print( 'Please upload pdf file.' )
                return False
        path = self.prePath+'/'+filenames[0][:-4].split('/')[-1]
        try:  
                os.mkdir(path)
        except OSError:  
                print ("Creation of the directory %s failed" % path)
                shutil.rmtree(path)
                os.mkdir(path)
                print ("Creation of the directory %s successful. Directory removed and recreated." % path)
        else:  
                print ("Successfully created the directory %s " % path)
        
        extractor = extract_images.Extract(path, filenames[0])
        self.window.parent.button1.Destroy()
        self.window.parent.drag_drop_area.Destroy()	
        self.window.parent.SetBackgroundColour('#FFFFFF')
        bigpanel = BigPanel(self.window.parent,path+'/'+filenames[0][:-4].split('/')[-1]+"-", extractor.cnt(filenames[0]))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add( bigpanel, 1, wx.ALL | wx.EXPAND, 15 )

        self.SetSizer( sizer )
        self.SetAutoLayout(1)
        self.SetupScrolling()
        return True  

class DnDPanel(sc.SizedPanel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.parent = parent

        file_drop_target = MyFileDropTarget(self, parent.prePath)
        lbl = wx.StaticText(self, label="Drag some files here:")
        self.fileTextCtrl = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY)
        self.fileTextCtrl.SetDropTarget(file_drop_target)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl, 0, wx.ALL, 5)
        sizer.Add(self.fileTextCtrl, 1, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(sizer)

class PDF_Panel(sc.SizedScrolledPanel):

	def __init__(self, parent):
		sc.SizedScrolledPanel.__init__(self, parent)
		self.SetBackgroundColour('#b95540')
		self.parent = parent

		self.prePath = os.getcwd()

		self.button1 = wx.Button(self, id = wx.ID_ANY, label = "Add Document")
		self.button1.SetSizerProps(halign="center")
		self.button1.Bind(wx.EVT_BUTTON, self.onButton)

		self.drag_drop_area = DnDPanel(self)
		self.drag_drop_area.SetSizerProps(halign="center")


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
			print("Hii file uploaded.")
		path = self.prePath+'/'+filename[:-4].split('/')[-1]
		try:  
			os.mkdir(path)
		except OSError:  
			print ("Creation of the directory %s failed" % path)
			shutil.rmtree(path)
			os.mkdir(path)
			print ("Creation of the directory %s successful. Directory removed and recreated." % path)
		else:  
			print ("Successfully created the directory %s " % path)
        
		extractor = extract_images.Extract(path, filename)
		self.button1.Destroy()
		self.drag_drop_area.Destroy()
		
		self.SetBackgroundColour('#FFFFFF')
		bigpanel = BigPanel(self,path+'/'+filename[:-4].split('/')[-1]+"-", extractor.cnt(filename))
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add( bigpanel, 1, wx.ALL | wx.EXPAND, 15 )

		self.SetSizer( sizer )
		self.SetAutoLayout(1)
		self.SetupScrolling()
		

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