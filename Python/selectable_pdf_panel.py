import wx
import wx.lib.sized_controls as sc
import os
import extract_images
import shutil

upload = False
p = ''

class Panel(wx.Panel):
    def __init__(self, parent,loc,i,cnt):
        wx.Panel.__init__(self, parent, size=(620,880*cnt))
        # several "Panels" sized added together 
        # are bigger than ScrolledPanel size

        self.SetMinSize( (600, 870) )
        
        img = wx.Image(loc+str(i)+".png", wx.BITMAP_TYPE_ANY)
        imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(img))
        imageCtrl.SetBitmap(wx.Bitmap(img))

class BigPanel(wx.Panel):
    def __init__(self, parent, loc, cnt):
        global upload 
        upload = True
        wx.Panel.__init__(self, parent, size=(620,880*cnt))

        img = []        
        for i in range(cnt):
            img.append(Panel(self,loc,i,cnt))

        sizer = wx.BoxSizer(wx.VERTICAL)

        for i in range(cnt):
            sizer.Add( img[i], 1, wx.ALL | wx.EXPAND, 2)
        
        self.SetSizer( sizer )

class MyFileDropTarget(wx.FileDropTarget):

    def __init__(self, window,prePath):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.prePath = prePath

    def OnDropFiles(self, x, y, filenames):
        global p
        print(filenames[0])
        
        if(filenames[0][-4:] != '.pdf'):
                print( 'Please upload pdf file.' )
                return False
        path = self.prePath+'/'+filenames[0][:-4].split('/')[-1]
        p = path
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
        bigpanel = BigPanel(self.window.parent,path+'/'+filenames[0][:-4].split('/')[-1]+"-", extractor.cnt()) 
        f= open(path+'/'+"selectable.txt","w+")
        f.write(extractor.getText())	
        f.close()
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
		global p
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
		p = path
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
		bigpanel = BigPanel(self,path+'/'+filename[:-4].split('/')[-1]+"-", extractor.cnt())
		f= open(path+'/'+"selectable.txt","w+")
		f.write(extractor.getText())	
		f.close()
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add( bigpanel, 1, wx.ALL | wx.EXPAND, 15 )

		self.SetSizer( sizer )
		self.SetAutoLayout(1)
		self.SetupScrolling()
