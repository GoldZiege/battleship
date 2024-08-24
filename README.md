# Battleship

This program is a modified version of the classic board game battleships in which you atke the role of a battleship commander that has to attack enemy ships with limited ammunition.

The app turns battleships into a one sided game where you get all the fun of shooting at enemy ships without having to worry about your own ships.

[click here for the deployed project](https://battleship-commander-b2b519a74b77.herokuapp.com/)

## How to play

- At the start the user decides to jump right into the game or get an explanation first
- When the game starts the player sees the game grid without being able to see where the enemy ships are.
- Each turn the player shots at a chosen coordinate.
- Every shot gets marked on the game grid. Hits are marked with an 'X' and misses are marked with an 'O'.
- If the player succeeds in sinking all enemy ships within 18 turns they win. Otherwise they are out of ammunition and lose the game.

## Features 

### Welcome Screen:
- From the welcome screen the user can choose to access a short explanation text or start the game immediately.
    - The user has to enter either 'g' or 'e' otherwise an error message will show and the input is requested again.

![Screenshot of the welcome screen](docs/welcome-screen.png)

### Explanation:
- If the user chooses to see the explanation a text is shown on screen that explains everything the user needs to know to play the game.
- At the end the user is requested to press the 'Enter' key to return to the welcome screen
    - The user has to press enter without making any other inputs or an error message will show. The user is then requested again to press the 'Enter' key

![Screenshot of the explanation](docs/explanation.png)

### Game:
- The Ships are placed randomly so the game is different every time.
- The game grid is shown and the player is requested to input coordinates to fire at.

![Screenshot of the game grid](docs/game-grid.png)

- Input validation and error-checking:
    - The user cannot enter coordinates outside the game-grid
    - The user cannot enter a string longer or shorter than two characters
    - The user cannot enter an empty string
    - The user can user upper or lower case for letters

![Screenshot of error message](docs/input-validation.png)

- If the player looses the game they get to see where the ships were placed.

![Screenshot of a lost game](docs/lose-screen.png)

- At the end the user can do two things:
    - start a new game by entering 'g'
    - exit and go back to the welcome screen by entering 'e'

### Future Features
- Giving the user feedback when a ship is destroyed
    - Right now the user has to waste valuable shots to confirm a ships length
- Making it impossible to target the same coordinate twice
    - Right now it is possible to hit the same target repeatedly to cheat the game an win easily
- Giving the user the possibility to choose the grid size, the amount of ships and the amount of ammunition
    - That way the user can individually set their difficulty at their discretion

## Data Model

![Flowchart of the app](docs/ablauf.jpg)

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