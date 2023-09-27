import pandas as pd
import numpy as np

import os
from sklearn.model_selection import train_test_split
from data_transformation import DataTransformation

from dataclasses import dataclass
from data_transformation import DataTransformation

from model_training import ModelTrainer
from model_training import ModelTrainerConfig


@dataclass
class DataIngestionConfig:
	raw_csv_path = os.path.join('artifacts','raw.csv')
	train_csv_path = os.path.join('artifacts','train.csv')
	test_csv_path = os.path.join('artifacts','test.csv')
	
	
class DataIngestion:
	def __init__(self):
		self.art_file_path = DataIngestionConfig()
		
		
	def inetiate_data_en(self):		
		try:
		
			df = pd.read_csv("/storage/emulated/0/practice/data/WHR_2023.csv")
			
			os.makedirs(os.path.dirname(self.art_file_path.raw_csv_path),exist_ok=True)
			os.makedirs(os.path.dirname(self.art_file_path.train_csv_path),exist_ok=True)
			
			os.makedirs(os.path.dirname(self.art_file_path.test_csv_path),exist_ok=True)
			
			df.to_csv(self.art_file_path.raw_csv_path)
			
			train_data,test_data = train_test_split(df,test_size=0.2,random_state=42)
			
			train_data.to_csv(self.art_file_path.train_csv_path,index =False,header=True)
			test_data.to_csv(self.art_file_path.test_csv_path,index=False,header=True)
			
			return (
			
			self.art_file_path.train_csv_path,
			self.art_file_path.test_csv_path
		
		)
		
		except Exception as e:
			raise e
			
			
if __name__ == "__main__":
		
		obj = DataIngestion()
		train_data ,test_data = obj.inetiate_data_en()
		
		data_trans_obj = DataTransformation()		
		train_arr, test_arr = data_trans_obj.impliment_data_trans(train_data,test_data)
		
		model_trainer_obj = ModelTrainer()
		model_trainer_obj.initiate_model_trainig(train_arr=train_arr,test_arr=test_arr)
		
		print("Successfiull")
		
		
		
			
		
		
		
		
	
	