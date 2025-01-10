from src.Dimondpriceprediction.components.data_ingestion import DataIngestion
from src.Dimondpriceprediction.components.data_transformation import DataTransformation

from src.Dimondpriceprediction.logger import logging
from src.Dimondpriceprediction.exception import customexception

import os
import numpy as np
import sys

obj = DataIngestion()
train_data_path,test_data_path = obj.initiate_data_ingestion()

data_transformation = DataTransformation()
train_arr,test_arr = data_transformation.initaite_data_transformation(train_data_path,test_data_path)