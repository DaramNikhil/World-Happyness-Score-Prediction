from sklearn.linear_model import LinearRegression

from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
import dill
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

from utils import evaluate_models
from utils import save_object

from sklearn.metrics import r2_score
from utils import save_object

from dataclasses import dataclass
import pickle
import os


@dataclass
class ModelTrainerConfig:
	
	trained_model_path = os.path.join("artifacts","model.pkl")
	
class ModelTrainer:
	
	def __init__(self):
		self.trained_model_path = ModelTrainerConfig()
		
	def initiate_model_trainig(self,train_arr,test_arr):
		
		try:
		
			X_train = train_arr[:,:-1]
			y_train = train_arr[:,-1]
			X_test = test_arr[:,:-1]
			y_test = test_arr[:,-1]
			
			models = {
			
			"linear_regression":LinearRegression(),
			"Rf":RandomForestRegressor(),
			"Ada_boost":AdaBoostRegressor(),
			"Gradient_boost":GradientBoostingRegressor(),
			"Dt":DecisionTreeRegressor(),
			"Kneighbors":KNeighborsRegressor()
			
			
			}
			
			model_scores = evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
		models = models
		
		)
		
			best_model_score = max(sorted(model_scores.values()))
		
			best_model = max(sorted(model_scores))
			
			#saving object of best model
			save_object(
			
			best_model,
			self.trained_model_path.trained_model_path
			
			
			)
			
			prediction_fit = models[best_model].fit(X_train,y_train)
			
			predictions = prediction_fit.predict(X_test)
			
			#r2 score
			r2_score_ = r2_score(y_test,predictions)*100
			
					
			print(r2_score_)
			
		
		
			
		except Exception as e:
			raise e
		
		
		
		
	
		
		
	
	
	



