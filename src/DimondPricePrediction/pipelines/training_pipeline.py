from src.Dimondpriceprediction.components.data_ingestion import DataIngestion

from src.Dimondpriceprediction.logger import logging
from src.Dimondpriceprediction.exception import customexception

import os
import numpy as np
import sys

obj = DataIngestion()
obj.initiate_data_ingestion()