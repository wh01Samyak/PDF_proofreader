from wand.image import Image as wi

class Extract():
	def __init__(self,path, filename):
		self.openthefile(path,filename)
	
	def openthefile(self,path, fname):
		pdf = wi(filename = fname, resolution = 300)
		pdfImage = pdf.convert("jpeg")
		filename = fname[:-4]
		self.pagecnt = len(pdf.sequence)
		i=0
		for img in pdf.sequence:
			page = wi(image = img)
			page .save(filename = path+'/'+filename.split('/')[-1]+"-"+str(i)+".jpg")
			i = i+1
			
	def cnt(self):
		return self.pagecnt
