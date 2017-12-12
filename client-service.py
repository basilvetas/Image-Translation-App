from clarifai import rest
from clarifai.rest import ClarifaiApp
from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

## API to handle post requests for hot dog image prediction
class ModelHandler(RequestHandler):	
	def initialize(self, app):
		self.app = app		

	def set_default_headers(self):
		super(ModelHandler, self).set_default_headers()
		self.set_header('Access-Control-Allow-Origin', 'http://localhost:8080')
		self.set_header('Access-Control-Allow-Credentials', 'true')	

	def post(self):
		self.set_header("Content-Type", "text/plain")
		url = self.get_body_argument('url')    				
		count = self.get_body_argument('count')
		print("Count: ", count)
		if (int(count) == 0):
			prediction = predictImage(self.app, url)
			concepts = prediction['outputs'][0]['data']['concepts']
			results = {}
			for concept in concepts:
				results[concept['name']] = round(concept['value']*100, 2)
			print("Results: ", results)
			self.write(results)

		else:
			dog_prediction = predictDog(url)
			dog_breeds = dog_prediction['outputs'][0]['data']['concepts']
			results = {}
			for dog_breed in dog_breeds:
				results[dog_breed['name']] = round(dog_breed['value']*100, 2)
			self.write(results)

# Deletes old image inputs and models from the app object so we can re-train without conflict
# def clearApp(app):
# 	app.inputs.delete_all()
# 	app.models.delete_all()
# 	return app

# Uses images from dogs.csv to train the model, returns the app object with trained model
# def trainModel(app):	 
# 	print("Training Model...") # train model
# 	file = open("dogs.txt")
# 	lines = file.readlines()		

# 	for i, line in enumerate(lines):
# 		url = line.strip()
# 		app.inputs.create_image_from_url(url, image_id="id" + str(i), concepts=["dog"])		
	
# 	model = app.models.create("dogs", concepts=["dog"])		
# 	model = model.train()
# 	return app

# Predicts whether the image url param contains a hot dog, returns dict of results
def predictImage(app, url):
	print("Predicting Image...")
	model = app.models.get("general-v1.3")		
	pred = model.predict_by_url(url=url)
	return pred

def predictDog(url):
	print("Predicting Dog...")
	app = ClarifaiApp(api_key='c5c78def8d574935aebbfd8da2c22ed3')
	model = app.models.get('dogBreeds')
	pred = model.predict_by_url(url = url)
	return pred

# Trains the Clarifai app model, passes app object into request handler
def make_app():	
	app = ClarifaiApp(api_key=open("key.txt").read())
	# app = clearApp(app)
	# app = trainModel(app)		
	print("Server running on localhost:7777")
	return Application([
		(r"/predict/", ModelHandler, dict(app = app)),
	])

if __name__ == '__main__':	
	app = make_app()
	app.listen(7777)
	IOLoop.current().start()
