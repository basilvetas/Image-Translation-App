from clarifai import rest
from clarifai.rest import ClarifaiApp
from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

from config import API_KEY

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

# Predicts whether the image url param contains a hot dog, returns dict of results
def predictImage(app, url):
	print("Predicting Image...")
	model = app.models.get("general-v1.3")		
	pred = model.predict_by_url(url=url)
	return pred

def predictDog(url):
	print("Predicting Dog...")
	app = ClarifaiApp(api_key='c79df4e064e54afa88279b9600e63ea6')
	model = app.models.get('dogBreeds')
	pred = model.predict_by_url(url = url)
	return pred

# Trains the Clarifai app model, passes app object into request handler
def make_app():	
<<<<<<< HEAD:client-service.py
	app = ClarifaiApp(api_key=open("key.txt").read())			
=======
	app = ClarifaiApp(api_key=API_KEY)
	# app = clearApp(app)
	# app = trainModel(app)		
>>>>>>> 4918853eb16a64b74221ad9cdee2dbd54c9c0a78:image_recog_service/__main__.py
	print("Server running on localhost:7777")
	return Application([
		(r"/predict/", ModelHandler, dict(app = app)),
	])

if __name__ == '__main__':	
	app = make_app()
	app.listen(7777)
	IOLoop.current().start()
