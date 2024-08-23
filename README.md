# Battleship

## Deployment
- https://dashboard.heroku.com/apps
- click new at top of screen --> create new app
- fill in a name and choose a region
- click create app 
- go to the settings tab
- under config vars click on reveal config vars
- add a config var with key PORT and value 8000
- under buildpacks
- add the buildpacks python and nodejs in this order
- go to the Deploy tab
- under deployment method choose GitHub 
- confirm to connect to github
- use the searchbar that appears to search for your repository
- click connect on the right repository 
- under automatic deploys choose enable automatic deploys
- under manual deploy choose the branch from wich to deploy and click deploy branch
- click on view to get to the deployed site