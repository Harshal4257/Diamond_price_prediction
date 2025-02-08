from src.Dimondpriceprediction.components.data_ingestion import DataIngestion
from src.Dimondpriceprediction.components.data_transformation import DataTransformation
from src.Dimondpriceprediction.components.model_trainer import ModelTrainer
from src.Dimondpriceprediction.components.model_evaluation import ModelEvaluatuion

from src.Dimondpriceprediction.logger import logging
from src.Dimondpriceprediction.exception import customexception

import os
import sys
import numpy as np

obj = DataIngestion()
train_data_path,test_data_path = obj.initiate_data_ingestion()

data_transformation = DataTransformation()
train_arr,test_arr = data_transformation.initaite_data_transformation(train_data_path,test_data_path)

model_trainer = ModelTrainer()
model_trainer.initate_model_training(train_arr,test_arr)

model_evaluation = ModelEvaluatuion()
model_evaluation.initiate_model_evaluation(train_arr,test_arr)
