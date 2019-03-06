import sys, os
from ocr import format_conversions
from ocr.transcription import ocrpytesseract

sys.path.append('../ocr/')

pdf2png('doc_test.pdf')

txt, scr = jpg2text()
