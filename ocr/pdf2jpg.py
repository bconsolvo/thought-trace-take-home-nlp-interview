with Img(filename='doc_test.pdf', resolution=300) as img:
    img.compression_quality = 99
    img.save(filename='doc_test.jpg')
