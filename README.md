
----------To begin----------


Create a file called key.txt and copy the API key for Clarifai into the file

First install the client server globally with: 

	npm install http-server -g

The Tornado Web Server is located in the file client-service.py. To start server on localhost:7777:

	python3 client-service.py

(note sometimes the first time you run the server Clarifai API responds with an error -- if this happens just re-run it)

The AngularJS Client is located in the file index.html. To start client on localhost:8080:

	http-server

Test URL: 

	http://www.eatlovesavor.com/wp-content/uploads/2012/02/paris-cafe-croissant-coffee-and-newspaper.png


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

