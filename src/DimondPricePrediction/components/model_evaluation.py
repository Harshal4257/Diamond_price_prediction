import os,sys
import numpy as np
import pandas as pd
import pickle
import mlflow
import dagshub

from src.Dimondpriceprediction.logger import logging
from src.Dimondpriceprediction.exception import customexception
from src.Dimondpriceprediction.utils.utils import load_object
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

              


class ModelEvaluatuion:
    def __init__(self):
        pass
    
    def eval_metric(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        
        return rmse,mae,r2
    
    def initiate_model_evaluation(self,train_arr,test_arr):
        try:
            x_test,y_test = (test_arr[:,:-1],test_arr[:,-1])
            
            model_path = os.path.join("artifacts","model.pkl")
            model = load_object(model_path)
            
            dagshub.init(repo_owner='harshal_42',
             repo_name='Diamond_price_prediction',
             mlflow=True)
            mlflow.set_registry_uri("https://dagshub.com/Harshal_42/Diamond_price_prediction.mlflow")
            
            with mlflow.start_run():
                y_pred = model.predict(x_test)
                (rmse,mae,r2) = self.eval_metric(y_test,y_pred)
                
                mlflow.log_metric("RMSE",rmse)
                mlflow.log_metric("MAE",mae)
                mlflow.log_metric("R2",r2)
                    
        except Exception as e:
            raise customexception(e,sys)