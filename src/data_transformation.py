import numpy as np
import os
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
import dill
from utils import save_object



@dataclass
class DataTransformationConfig:
	process_file_path = os.path.join('artifacts','preprocess.pkl')
		
class DataTransformation:
	def __init__(self):
		self.process_file_path = DataTransformationConfig()
	
		
	def preprocessing_obj(self):
		
		try:
			
			numaric_columns = [
						
			"gdp_per_capita","social_support","healthy_life_expectancy","freedom_to_make_life_choices","generosity","perceptions_of_corruption"
			
			]
			
			
			numaric_pipeline = Pipeline(
			
			[
			
			("imputer",SimpleImputer(strategy='mean')),
			("scaler",StandardScaler())
			
			]
			
			)
			
			
			preprocessor = ColumnTransformer(
			
				[
				("numaric_pipeline",numaric_pipeline,numaric_columns)
				],remainder="passthrough"	)
				
			return preprocessor
			
		except Exception as e:
			raise e
			
	#implimentation datatransformation		
	def impliment_data_trans(self,train_csv,test_csv):
		try:	
				train_df = pd.read_csv(train_csv)
				test_df = pd.read_csv(test_csv)
				
				processor_object = self.preprocessing_obj()
				
				
				
				#train			
				train_feature = train_df.drop(["happiness_score","country","region"],axis=1)
				
				target_train_feature= train_df["happiness_score"]
				
				#test
				test_feature = test_df.drop(["happiness_score","country","region"],axis=1)
				
				test_target_feature= test_df["happiness_score"]
				
				#train array preprocess
				train_feature_arr = processor_object.fit_transform(train_feature)
				
				#train array preprocess
				test_feature_arr = processor_object.transform(test_feature)
				
				train_arr = np.c_[
				
				train_feature_arr,np.array(target_train_feature)
				
				]
				
				test_arr = np.c_[
				
				test_feature_arr,np.array(test_target_feature)
				
				]
				
				save_object(
					processor_object,
					self.process_file_path.process_file_path)	
				
				return(
				
				train_arr,
				test_arr,
			
			)
			
			
		except Exception as e:
			raise e
			
			
			
			
			
			
			

			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			

			
			
			
			
			