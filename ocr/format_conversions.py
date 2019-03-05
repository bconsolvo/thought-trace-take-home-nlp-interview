# Converts a PDF to multiple JPG files (1 for each page)

from wand.image import Image as Img

def pdf2png(pdffile):
    new_title = pdffile.split('.')[-2] + '.jpg'
    with Img(filename=pdffile, resolution=300) as img:
        img.compression_quality = 99
        img.save(filename=new_title)
