import sys, os

#sys.path.append('../ocr')


from src import formatconversions
from src.transcription import ocrpytesseract
from src import conftranscription

#Wand and Imagemagick is having difficulties reading the PDF
# formatconversions.pdf2png('src/doc_test.pdf')


# Must specify the path of pytesseract, but cannot figure out the path for Travis CI
a = ocrpytesseract() #must initiate the class before it can be used.
txt_strings, score_tbl = a.jpg2text('src/')
#print(txt_strings)
#print(score_tbl)


master,grade = conftranscription.ocrall('src/doc_test_ocr.csv','src/valid_words.txt')
print(master)
print(grade)
