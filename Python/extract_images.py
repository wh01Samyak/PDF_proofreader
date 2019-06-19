# Source - https://pymupdf.readthedocs.io/en/latest/tutorial/
import fitz

class Extract():
	def __init__(self,path, filename):
		self.openthefile(path,filename)
	
	def openthefile(self,path, filename):
		doc = fitz.open(filename)
		filename = filename[:-4]
		self.pagecnt = doc.pageCount
		self.text = ''
		for i in range(self.pagecnt):
			page = doc.loadPage(i)
			pix = page.getPixmap()
			pix.writePNG(path+'/'+filename.split('/')[-1]+"-"+str(i)+".png")
			self.text = self.text + page.getText("text") +'\n'

	def cnt(self):
		return self.pagecnt

	def getText(self):
		return self.text
