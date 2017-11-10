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

