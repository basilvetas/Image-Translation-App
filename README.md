
----------To begin----------

1. Create a file called config.py in the image_recog_service/ directory and copy the following into the file, filling in your Clarifai API Key where instructed:
	
	API_KEY="YOUR-API-KEY-GOES-HERE"

2. Create a file called config.py in the translation_service/ directory and copy the following into the file, filling in your Google Translate API Key where instructed:
	
	API_KEY="YOUR-API-KEY-GOES-HERE"

3. Create a file called config.py in the dog_recog_service/ directory and copy the following into the file, filling in your Clarifai API Key where instructed:
	
	API_KEY="YOUR-API-KEY-GOES-HERE"

4. Create a file called config.py in the text_to_speech_service/ directory and copy the following into the file, filling in your IBM API Key and Password where instructed:
	
	USERNAME="YOUR-API-KEY-GOES-HERE"
	PASSWORD="YOUR-PASSWORD-GOES-HERE"

5. Install the client server globally with: 

	npm install http-server -g

6. To start client on localhost:8080, from the client directory run:

	http-server

7. For each of the services, using the respective port, run:

	docker build -t some-image-name .
	docker run -p PORT:PORT some-image-name

