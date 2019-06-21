import pytesseract
from pytesseract import Output
import cv2

def highlight(fileName, word, prevWord):
	img = cv2.imread(fileName)

	d = pytesseract.image_to_data(img, output_type=Output.DICT)
	n_boxes = len(d['level'])
	prev = ''

	for i in range(n_boxes):

		if(d['level'][i] == 5 and d['text'][i] == word and prev == prevWord ):
			(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
			cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

			alpha = 0.6
			overlay = img.copy()
			output = img.copy()

			cv2.rectangle(overlay, (x, y), (x + w, y + h), (0, 0, 255), -1)
			cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
			return output

		if(d['level'][i] == 5):
			prev = d['text'][i]


