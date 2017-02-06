import media
import fresh_tomatoes
import webbrowser
import urllib.request
import requests

# API KEY, URL TEMPLATES AND YEAR OF THE MOVIE LIST

API_KEY = "2178202FC1DB6B1A582DF6C7FA1E4CFE"
requested_movie_year = str(2014)
URL = "http://api.cinemalytics.in/v2/movie/year/" + requested_movie_year + "/?auth_token=" + API_KEY

check_for_site_availability = requests.get(URL)
site_status_code = check_for_site_availability.status_code
if(site_status_code == 200):
	response_json = requests.get(URL).json() #GET MOVIE LIST TO JSON


	i = 0
	objects_from_listings = []

	# GOING THROUGH ALL THE JSON DATA AND STORING ACCORDINGLY TO EACH OBJECT IN AN OBJECT ARRAY
	for i in range(0,len(response_json)):
		objects_from_listings.append(media.Movie(response_json[i]['Title'],
													response_json[i]['Description'],
													response_json[i]['PosterPath'],
													response_json[i]['TrailerLink']))
		i = i + 1

	# COPYING TO NEW OBJECT ARRAY
	movies = objects_from_listings
	fresh_tomatoes.open_movies_page(movies)
else:
	print("Connection Error. Check the API Key")