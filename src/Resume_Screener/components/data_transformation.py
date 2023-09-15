import sys
import numpy as np 
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import tokenize
from src.Resume_Screener.exception import CustomException
try:
   
    from src.Resume_Screener.exception import CustomException
    print("numpy is available.")
except ImportError:
    print("numpy is not available.")
from src.Resume_Screener.logger import logging
import os

from src.Resume_Screener.utils import cleanResume

import re
def cleanResume(resumeText):
    try :
        resumeText = re.sub('http[\S+\s]*', ' ', resumeText)  # remove URLs
        resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
        resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
        resumeText = re.sub('@\S+', '  ', resumeText)  # remove mentions
        resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # remove punctuations
        resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText) 
        resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
        # resumeData['cleaned_resume'] = resumeData.Resume.apply(lambda x: cleanResume(x))
        # resumeData['cleaned_resume'] = resumeData['cleaned_resume'].str.lower() 
        # stopword_list = set(stopwords.words('english')+['``',"''"])
        # resumeData.cleaned_resume=resumeData.cleaned_resume.apply(lambda x : " ".join(x for x in x.split() if x not in stopword_list))
        # resumeData['cleaned_resume']=resumeData.cleaned_resume.apply(word_tokenize)
        # lemmatizer=WordNetLemmatizer()
        # resumeData['cleaned_resume']=resumeData.cleaned_resume.apply(lambda x:[lemmatizer.lemmatize(word) for word in x])
        # resumeData.cleaned_resume= resumeData.cleaned_resume.astype(str)
        # cleaned_resume_list=resumeData['cleaned_resume'].array
        return resumeText
    except Exception as e:
        raise CustomException(e,sys)
  
class DataTransformation:
   

    def get_data_transformer(self,resumeData):
        '''
        This function si responsible for data trnasformation
        
        '''
        try:

            resumeData['cleaned_resume'] = resumeData.Resume.apply(lambda x: cleanResume(x))
            resumeData['cleaned_resume'] = resumeData['cleaned_resume'].str.lower() 
            stopword_list = set(stopwords.words('english')+['``',"''"])
            resumeData.cleaned_resume=resumeData.cleaned_resume.apply(lambda x : " ".join(x for x in x.split() if x not in stopword_list))
            resumeData['cleaned_resume']=resumeData.cleaned_resume.apply(word_tokenize)
            lemmatizer=WordNetLemmatizer()
            resumeData['cleaned_resume']=resumeData.cleaned_resume.apply(lambda x:[lemmatizer.lemmatize(word) for word in x])
            resumeData.cleaned_resume= resumeData.cleaned_resume.astype(str)
            # cleaned_resume_list=resumeData['cleaned_resume'].array
            # return cleaned_resume_list
            print(resumeData.head())
            return resumeData
    
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            train_df=self.get_data_transformer(train_df)
            test_df=self.get_data_transformer(test_df)

         

        

            return (
                (train_df),
               (test_df)
            )
        except Exception as e:
            raise CustomException(e,sys)