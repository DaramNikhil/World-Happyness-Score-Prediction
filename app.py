from flask import Flask,render_template,url_for,request
#from src.utils import load_path
from src.pipeline.prediction_pipeline import get_data_template
from src import artifacts 
import pickle
from src import utils


APP = Flask(__name__,template_folder="templates")


@APP.route("/",methods=["POST","GET"])
def home_page():
	
	if request.method == "POST":
		
		gdp_per_capita = float(request.form["gdp_per_capita"])
		
		social_support = float(request.form["social_support"])
		
		healthy_life_expectancy = float(request.form["healthy_life_expectancy"])
		
		freedom_to_make_life_choices = float(request.form["freedom_to_make_life_choices"])
		
		generosity = float(request.form["generosity"])
		
		perceptions_of_corruption = float(request.form["perceptions_of_corruption"])
		
		
		
		data = get_data_template(
		
		gdp_per_capita,
		social_support,
		healthy_life_expectancy,
		freedom_to_make_life_choices,
		generosity,
		perceptions_of_corruption		
		
		)
		
		
		pred =  data.get_data_as_df()
		
		#fitted_model 
		with open("/storage/emulated/0/nation_happyness_score_prediction/src/artifacts/fitted_model.pkl","rb") as f:
	
			f_model = pickle.load(f)
			
		#scaling model	
		with open("/storage/emulated/0/nation_happyness_score_prediction/src/artifacts/preprocess.pkl","rb") as scale:
			
			#load the processing scale
			scale = pickle.load(scale)
			
			#scaling the data			
		transform_pred  = scale.transform(pred)
			
			#transforming the data
		prediction = f_model.predict(transform_pred)
			
			#predictions
		main_pred = round(prediction[0],3)
			
		return render_template('prediction.html',main_pred=main_pred)
		
		
	else:		
		return render_template("home.html")
	


if __name__ == "__main__":
	
	APP.run(host="0.0.0.0",debug=True)