import numpy as np
import pickle
from src import artifacts

with open(artifacts,'rb') as f:
	
	load_data = pickle.load(f)
	
	my_array = np.array([0.561,0.628,0.137,0.54,0.154,0.14]).reshape(-1,1)
	prer = load_data.predict(my_array)
	
	print(prer)
	
	
