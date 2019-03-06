from PIL import Image
import pytesseract
from pytesseract import Output
import glob
import pandas as pd
import numpy as np


class ocrpytesseract:
    #def __init__(self, drc):
    #    self.drc = drc
    #im_list = sorted(glob.glob('files/*.jpg'))
    
    def jpg2text(self,drc):
        im_list = sorted(glob.glob(drc+'*.jpg'))
        lst_text = []
        for i in im_list:
            imjpg = Image.open(i) # Opening the image with PIL
            print('Transcribing text')
            text = pytesseract.image_to_string(imjpg) # Uses trained model from Tesseract to convert JPG image to a string of text
            scores = pytesseract.image_to_data(imjpg, output_type=pytesseract.Output.DATAFRAME) # scores for each word transcribed
            #text_conf = scores[['text','conf']] # Extracting only the text and associated scores dataframe
            mean1 = scores.conf.replace(-1,np.NaN).mean() # Taking the mean confidence value over each word in the transcription
            print('The mean confidence value is', mean1,'. Transcription complete!')
            lst_text.append(text)
        # Saving the text to a dataframe, and then writing out a CSV to be used in the confidence function later.
        df = pd.DataFrame(lst_text)
        df.to_csv('pyt_output.csv',index=False,header=None)
        return lst_text, scores
