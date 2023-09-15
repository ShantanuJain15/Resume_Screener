import os
import sys
from dataclasses import dataclass


from src.Resume_Screener.exception import CustomException
from src.Resume_Screener.logger import logging

from src.Resume_Screener.utils import save_object
from sklearn.metrics import accuracy_score

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
        
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array.iloc[:,2].values,
                train_array.iloc[:,0].values,
                test_array.iloc[:,2].values,
                test_array.iloc[:,0].values
            )
           
            final = Pipeline([('Vect',TfidfVectorizer()), ('model',SVC(probability=True))])
            final.fit(X_train,y_train)
            y_pred=final.predict(X_test)
            print(accuracy_score(y_pred,y_test))

            logging.info(f"loading model")
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=final
            )
            logging.info(f"loaded model")

            return (accuracy_score(y_pred,y_test))



            
        except Exception as e:
            raise CustomException(e,sys)