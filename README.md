
----------To begin----------

1. Create a file called key.txt and copy the API key for Clarifai into the file

2. Create a file called config.py in the translation_service/ directory and copy the following into the file, filling in your Google Translate API Key where instructed:
	
	API_KEY="YOUR-API-KEY-GOES-HERE"

3. Create a file called config.py in the text_to_speech_service/ directory and copy the following into the file, filling in your IBM API Key and Password where instructed:
	
	USERNAME="YOUR-API-KEY-GOES-HERE"
	PASSWORD="YOUR-PASSWORD-GOES-HERE"

4. Install the client server globally with: 

	npm install http-server -g

5. The Image Recognition Tornado Web Server is located in the file client-service.py. To start server on localhost:7777:

	python3 client-service.py

6. The Translation Tornado Web Server is located in the file translation_service/translation_service/__main__.py. To start server on localhost:5001:

	python3 -m translation_service

7. The AngularJS Client is located in the file index.html. To start client on localhost:8080:

	http-server








----------Git workflow----------

IMPORTANT: Never work on master branch locally. Never push to master branch.  

Create and checkout new branch (b flag is for new branch):

	git checkout -b BRANCH-NAME

Stage files that have been edited:

	git add .

Commit locally (m flag for message):

	git commit -m "COMMIT MESSAGE HERE"

To be safe, always pull from master before pushing to keep any merge conflicts local:

	git pull origin master

If there were merge conflicts, recommit. Then push to remote branch:

	git push origin BRANCH-NAME

(Remotely - make Pull Request to merge branch with master)

----------Other useful commands----------

Checkout existing branch:

	git checkout BRANCH-NAME

Check status to check what branch you're on

	git status

Check available local and remote branches (a flag for list all)

	git branch -a

