import sys, os

#sys.path.append('../ocr')


from ocr import formatconversions
from ocr.transcription import ocrpytesseract


formatconversions.pdf2png('files/doc_test.pdf')


a = ocrpytesseract()
txt, scr = a.jpg2text('files/')
