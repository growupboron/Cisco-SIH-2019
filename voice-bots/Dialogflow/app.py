from flask import Flask
from flask_assistant import Assistant, tell
import requests 

import logging
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)

app = Flask(__name__)
assist = Assistant(app, project_id='GOOGLE_CLOUD_PROJECT_ID')

@assist.action('get-weather')
def hello_world():
     
    URL = "http://api.icndb.com/jokes/random"


# sending get request and saving the response as response object 
    r = requests.get(url = URL) 

# extracting data in json format 
    data = r.json() 


# extracting latitude, longitude and formatted address 
# of the first matching location 
    joke= data['value']['joke']

    #file1= open('joke.txt','w') 
    #file1.write(joke) 
    #file1.close() 
    # to see the full request and response objects
    # set logging level to DEBUG
    speech = joke
    return tell(speech)

if __name__ == '__main__':
    app.run(debug=True)