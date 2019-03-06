import sys, os

#sys.path.append('../ocr')


from ocr import formatconversions
from ocr.transcription import ocrpytesseract


formatconversions.pdf2png('tests/doc_test.pdf')

#txt, scr = jpg2text()
