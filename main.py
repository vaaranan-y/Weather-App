import random
from tkinter import *
import requests
import json
#from PIL imageTK, Image

# root is the basis of the window in this GUI application
root = Tk()
# set dimensions
root.geometry("300x300")
root.title("Weather App")
#root.iconbitmap(image file directory goes here)

# Example: adding a label to the window
title = Label(root, text="Weather App")
title.pack()
signal = Label(root, text="Current Weather")
signal.pack()

def buttonFunction():
	print("Hello World!")
	#Test
	#signal["text"] = "Updated: " + str(random.randint(0,100))
	#Toronto API
	api_request = requests.get("https://api.weatherbit.io/v2.0/current?&city=Toronto,Ontario&key=e329732da2bd48a89a0691a66d9f8b37")

        #Test API
	#api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=ab4d2f4017ae0137e2abb88cc1b43fc0")
	
	
	api = json.loads(api_request.content)
	signal["text"] = "Current temperature: " + str(api["data"][0]["temp"]) + "\nTime of Request: " + str(api["data"][0]["ob_time"])



b = Button(root, text="Update", command=buttonFunction)
b.pack(side=RIGHT)


# This will hold the view in place, makes it viewable, and closes it when prompted
# It stays at the end of file
root.mainloop()
