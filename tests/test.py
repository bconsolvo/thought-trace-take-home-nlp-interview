import sys
sys.path.append('../ocr/')
from ocr import format_conversions
from ocr.transcription import ocrpytesseract

pdf2png('doc_test.pdf')

txt, scr = jpg2text()
scr
