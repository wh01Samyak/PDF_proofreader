# Source - https://pymupdf.readthedocs.io/en/latest/tutorial/
import fitz

class Extract():
	def __init__(self,path, filename):
		self.openthefile(path,filename)
	
	def openthefile(self,path, filename):
		doc = fitz.open(filename)
		filename = filename[:-4]
		pagent = doc.pageCount
		for i in range(pagent):
			page = doc.loadPage(i)
			#page = doc[n]
			pix = page.getPixmap()
			pix1 = page.getSVGimage()
			pix.writePNG(path+'/'+filename.split('/')[-1]+"-"+str(i)+".png")
			#pix.writePNG(filename+"-{i}.png")

# in wxPython bitmap = wx.Bitmap.FromBufferRGBA(pix.width, pix.height, pix.samples)

			#text = page.getText("text")

# searching fortext, making boxes = areas = page.searchFor("mupdf", hit_max = 16)


