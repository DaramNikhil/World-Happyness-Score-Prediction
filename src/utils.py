import os
import dill
import pickle
from sklearn.metrics import r2_score

def save_object(processor,file_path):
	try:
		
		path_obj = os.path.dirname(file_path)
		os.makedirs(path_obj,exist_ok=True)
		
		with open(file_path,'wb') as f:
			pickle.dump(processor,f)	
			
					
	except Exception as e:
		raise e
		
		
def evaluate_models(X_train,y_train,X_test,y_test,models
		):
			
	try:
			
		report = {}
		
		for i in range(len(list(models))):
			model = list(models.values())[i]		
			model.fit(X_train,y_train)
				
			train_pred = model.predict(X_train)
				
			test_pred = model.predict(X_test)
				
			train_model_score = r2_score(y_train,train_pred)
				
			test_model_score = r2_score(y_test,test_pred)
				
			report[list(models.keys())[i]]=test_model_score

		return report
		
		
	except Exception as e:
		raise e
		
			
	
		
		
		
			
		
			