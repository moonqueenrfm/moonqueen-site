Simple static website using [Flask](https://flask.palletsprojects.com/en/3.0.x/#) framework<br/>
Styling is from Alex Rutar's ["How to Build a Personal Webpage from Scratch"](https://rutar.org/writing/how-to-build-a-personal-webpage-from-scratch/) blog post

## Setup
1. Ensure Python is installed on your machine
2. Clone this repository to your machine
3. Navigate to your repository folder in a terminal, then run the following commands:
```
$python3 -m venv .venv
$. .venv/bin/activate
$pip install Flask
$flask --app flaskapp.py run --debug
```
The above sequence of commands will ensure a virtual python environment is created for the project. Flask will be installed as part of the virtual environment. A virtual environment avoids collisions with other projects using Python. `$. .venv/bin/activate` will have to be ran every time you begin development. These steps were taken from the [Flask installation](https://flask.palletsprojects.com/en/3.0.x/installation/) page. 