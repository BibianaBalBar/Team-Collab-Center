# Team Collab Center

Python and Flask teams communication work tool.

Users can post their work issues and comment on posts by colleagues, from their or all work teams, to provide help.

![teamcollab](https://github.com/BibianaBalBar/Team-Collab-Center/blob/master/img/teamcollab.gif)

## Deployed at: 

https://team-collab-center.herokuapp.com/

To test it create your own user or use:\
Username: Peter\
Password: peter

## To run in your local server:

Requirements: Python 3.6+, python-pip, virtualenv

Clone this repo:
        
        $ git clone https://github.com/BibianaBalBar/Team-Collab-Center

        $ cd Team-Collab-Center


Create Virtual enviroment:
        
        $ python3 - venv env

        $ source env/bin/activate

        (env) $ 

Install all requirements:
        
        $ pip install -r requirements.txt

Set flask environment: (for windows use set command)

        (env) $ export FLASK_APP=team_collab.py

Run the app:

        (env) $ flask run

Access url to see web app

        http://localhost:5000/

## Search Engine
To enable the search option please refer the Elasticsearch installation tutorial here.

Run Elasticsearch:

        cd c:\elasticsearch-7.6.2

        .\bin\elasticsearch.bat

