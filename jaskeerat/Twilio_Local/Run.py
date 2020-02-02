import requests 
from googletrans import Translator
translator = Translator() 
URL = "http://api.icndb.com/jokes/random"
def msgSending(message):
	from twilio.rest import Client 
	 
	account_sid = 'ACce5e20a79c2c16f275856cea612a7d3c' 
	auth_token = '5b64af2e5956249e6774ba825a093e92' 
	client = Client(account_sid, auth_token) 
	 
	message = client.messages.create( 
	                              from_='+14064009801',  
	                              body=message,      
	                              to='+919814464733' 
	                          ) 
	 
	print(message.sid)


# sending get request and saving the response as response object 
r = requests.get(url = URL) 

# extracting data in json format 
data = r.json() 


# extracting latitude, longitude and formatted address 
# of the first matching location 
joke= data['value']['joke']
print(joke)

hindi=translator.translate(joke, dest='hi').text
print(hindi)
msgSending(message=hindi)
hindi=translator.translate(joke, dest='mr').text
print(hindi)
msgSending(message=hindi)
hindi=translator.translate(joke, dest='pa').text
print(hindi)
msgSending(message=hindi)
hindi=translator.translate(joke, dest='ru').text
print(hindi)
msgSending(message=hindi)
hindi=translator.translate(joke, dest='ta').text
print(hindi)
msgSending(message=hindi)

