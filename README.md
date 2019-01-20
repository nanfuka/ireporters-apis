# i-reporter

# description
I-reporter is the localised solution to the corruption problem in Africa. With this application, every citizen can  bring any form of corruption to the notice of the appropriate authorities. These have been termed as redflags in this application. The general public can also report interventions to the concerned authorities. Interventions can include issues such as a collapsed bridge.

## Project Features
- Create a ​red-flag​​ record
- Get all ​red-flag
​- Get a specific ​red-flag​​ record
- Edit a specific ​red-flag​​ record
- Delete a ​red-flag​​ record

## heroku
The app is hosted on heroku at [ireporter-api](https://reportth.herokuapp.com/)

## gh-pages 
- Go to [I-reporter](https://nanfuka.github.io/iReporter/)

## API endpoints for the application

| METHOD   | URL  | FUNCTIONALITY |
|---|---|---|
| GET |  `api/v1/red-flags` | Fetch all ​red-flag ​​records |
| GET | `api/v1/red-flags/<redflag_id>`| Fetch a specific ​red-flag​​ record |
| POST |  `api/v1/red-flags` | Create a ​red-flag​​ record |
| PATCH |  `api/v1/red-flags/<red-flag_id>/location` | Edit the location of a specific red-flag |
| PATCH |  `api/v1/red-flags/<red-flag_id>/comment` | Edit the comment of a specific red-flag record|
| DELETE | `api/v1/red-flags/<red-flag_id>/redflag` | Delete a specific red flag record
| POST |  `api/v1/signup` | Add user | 
| POST |  `api/v1/login` | login user |


## Instalation
- install python 3.7 or anyother version upwards.
- Clone the GitHub repo: git clone https://github.com/nanfuka/ireporter-api.git`
- git checkout develop
- install a virtualenviroment with these commands (virtualenv venv)
- move into the virtual enviroment.
- install the requred packages which are in the requrements.txt file by following these         commands in your tarminal(pip install -r requirements.txt)
- run the app (python run.py)


## Contributors
* Deborah Kalungi

## How to Contribute
1. Download and install Git
2. Clone the repo `https://github.com/nanfuka/ireporter-api.git`