import pandas as pd
import pickle

class ModelPrediction:
	def __init__(self):
		pass
		
				
class get_data_template:
	def __init__(self,gdp_per_capita,
		social_support,
		healthy_life_expectancy,
		freedom_to_make_life_choices,
		generosity,
		perceptions_of_corruption
		):
			
		self.gdp_per_capita = gdp_per_capita
			
		self.social_support = social_support
			
		self.healthy_life_expectancy = healthy_life_expectancy
			
		self.freedom_to_make_life_choices = freedom_to_make_life_choices
			
		self.generosity = generosity
			
		self.perceptions_of_corruption = perceptions_of_corruption
	
	#dataframing function		
	def get_data_as_df(self):
			
		df ={ "gdp_per_capita":int(self.gdp_per_capita),
			
						"social_support":int(self.social_support),
						"healthy_life_expectancy":int(self.healthy_life_expectancy),
						"freedom_to_make_life_choices":int(self.freedom_to_make_life_choices),
						"generosity":int(self.generosity),
						"perceptions_of_corruption":int(self.perceptions_of_corruption)
						
			}
			
			
		dframe = pd.DataFrame(df,index=[0])

			
		#return the data frame to app.py 	
		return dframe
	
			
			
			
			
		
		