import pandas as pd
import numpy as np

def ocrall(ocr_csv,dct_csv):
    #### Reading in the OCR output and words dictionary ####
    ocr_o = pd.read_csv(ocr_csv,names = ["Text"]) # Each line is a new paragraph in this OCR output.
    dct_o = pd.read_csv(dct_csv,names = ["Words"]) # Reading in the dictionary of words
    dct_o = dct_o['Words'].tolist() # Make the words dictionary dataframe into a list.
    #ocr_o.head() # display first 5 lines of the transcribed paragraphs
    
    #### PREPROCESSING OF THE TRANSCRIPTION OUTPUT ####
    '''
    Because the provided word dictionary only contains lower case words, with no numbers, and no punctuation, 
    we must preprocess the CSV file before evaluating it to match the word dictionary. We must:
        1. Remove all punctuation
        2. Remove all digits
        3. Replace more than 1 space with 1 space
    '''
    ocr_lc = pd.DataFrame(ocr_o['Text'].str.lower()) # Put all words in lower case
    ocr_lc['Text'] = ocr_lc['Text'].str.replace('[^\w\s]','') # remove all punctuation from text string
    ocr_lc['Text'] = ocr_lc['Text'].str.replace('_','') # removes all underscores _ from text 
    ocr_lc['Text'] = ocr_lc['Text'].str.replace('\d+', '') # remove all numbers
    ocr_lc['Text'] = ocr_lc['Text'].str.strip() # removes leading and end soaces from strings
    
    # For loop to reduce multiple spaces to 1 space for all strings
    lst_0 = []
    for i in ocr_lc['Text']:
        a = ' '.join(i.split())
        lst_0.append(a)
    se_1 = pd.Series(lst_0)
    ocr_lc['Text'] = pd.Series(lst_0)
    '''
    ### Not currently used
    ### Optional for loop to limit word length to eliminate short 1-2 letter words from OCR output
    lst_1 = []
    for i in se_1:
        b = ' '.join( [w for w in i.split() if len(w)>2] )
        lst_1.append(b)
    lst_1
    '''
    #### Write out the preprocessed text file ####
    out_csv = ocr_csv.split('.')[-2] + '_preproc.csv'
    ocr_lc.to_csv(out_csv,index=False) #Write out the preprocessed CSV file for QC
    ocr_lc.head() # Display top 5 lines of preprocessed text
    
    #### Calculating statistics on words and putting into a master dataframe ####
    ocr_master = pd.DataFrame(ocr_lc['Text'].str.split()) # split words in each row by commas to make lists
    l1 = ocr_master['Text'].tolist() # converting the dataframe column Text into a list type
    word_totals = list(map(len,l1)) # getting the length of each row of list of words
    se = pd.Series(word_totals) # converting list to series
    ocr_master['word_totals'] = se.values # inserting the word totals into the dataframe ocr_split
    #ocr_master.head() # Displaying first 5 lines of new dataframe.
    ser1 = ocr_master['Text']
    lst1 = []
    for i in ser1:
        countw = len(set(i) & set(dct_o)) #Key line for comparing words in each row to the words in the dictionary
        lst1.append(countw) # Putting the count into a list
    se_wc = pd.Series(lst1) # Making the lst1 with the count into a series before putting into the dataframe
    
    ocr_master['matching_words'] = se_wc.values # Adding the number of matching words as a column in the master dataframe
    ocr_master['d'] = ocr_master['matching_words'] / ocr_master['word_totals'] # A straight percentage grade for each paragraph detected
    
    ocr_master['all_words'] = ocr_master['word_totals'].sum() # Total of all words
    ocr_master['weight'] = ocr_master['word_totals'] / ocr_master['all_words'] # Weight for each set of words
    ocr_master['weighted_grade'] = ocr_master['d'] * ocr_master['weight'] # Weighted grade for each set of words
    #ocr_master # Displaying the new data-frame with the new statistics columns
    final_grade = 100 * ocr_master['weighted_grade'].sum() # Adding all of the weighted grades for a final score
    final_grade = round(final_grade) # final confidence out of 100 for the whole document
    return ocr_master, final_grade
