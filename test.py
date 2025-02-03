import importlib

try:
    module = importlib.import_module('src.Dimondpriceprediction.pipelines.prediction_pipeline')
    print("Module loaded successfully!")
except ModuleNotFoundError as e:
    print(f"Error: {e}")