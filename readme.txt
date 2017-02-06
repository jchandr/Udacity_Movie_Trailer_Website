Fresh Tomatoes is an application that list all the Bollywood movies that was released in particular year set by the code. This application is build with the help of Cinemalytics API Trial version, which can be found at https://developers.cinemalytics.com . The API key valid only for 3 days after the generation. The present API key is valid until Feb 9,2017 09:00 HRS PST.

Before starting the site, please make sure the API Key is valid. If has expired, please contact me to get a new API key. After getting the new API Key, please paste it as the value for the variable "API_KEY" present in the python file "entertainment_center.py".
For Example,
	
	API_KEY = "2178202FC1DB6B1A1N4IIF87FA1E4CFE"

You can even alter the movie list's year by changing the value of the variable "requested_movie_year" to a year that you want. For example 

	requested_movie_year = str(2012)

To Start the site, just go a terminal and type
	
	python entertainment_center.py