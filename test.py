import sys, os

#sys.path.append('../ocr')


from src import formatconversions
from src.transcription import ocrpytesseract
from src import conftranscription

# formatconversions.pdf2png('files/doc_test.pdf')



a = ocrpytesseract()
txt_strings, score_tbl = a.jpg2text('files/')
print(txt_strings)
print(score_tbl)


master,grade = conftranscription.ocrall('files/doc_test_ocr.csv','files/valid_words.txt')
print(master)
print(grade)
