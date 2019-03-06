import sys, os

#sys.path.append('../ocr')


from ocr import formatconversions
from ocr.transcription import ocrpytesseract
from ocr.confidence import conftranscription

formatconversions.pdf2png('files/doc_test.pdf')



#a = ocrpytesseract()
#txt, scr = a.jpg2text('files/')


master,grade = conftranscription.ocrall('files/doc_test_ocr.csv','files/valid_words.txt')
print(master)
print(grade)
