import pickle
import requests as re
from googleplaces import GooglePlaces,types,lang

apiKey = "AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY"

# placesToSee = re.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=12.972442,77.580643&radius=200000&keyword=places+to+see&key=AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY')

centralRest = re.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=12.972442,77.580643&radius=10000&keyword=restaurants&key=AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY')
forumRest = re.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=12.9347893,77.6101245&radius=10000&keyword=restaurants&key=AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY')
royalRest = re.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=12.8759575,77.5934378&radius=10000&keyword=restaurants&key=AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY')
rajajiRest = re.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=12.9947452,77.5345258&radius=10000&keyword=restaurants&key=AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY')
indiraRest = re.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=12.9729803,77.6294788&radius=10000&keyword=restaurants&key=AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY')

# resInJson = placesToSee.json()
# placesRes = resInJson['results']

# placesToSeeReviews = {}
# print("No of places found:{0}".format(len(placesRes)))
# csv place_id,review1,review2,review3,review4,review5
# for place in placesRes:
# 	tempRes = re.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+place['place_id']+'&key=AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY')
# 	tempResJson = tempRes.json()
# 	tempResJsonRes = tempResJson['result']

# 	temp = []
# 	for review in tempResJsonRes['reviews']:
# 		temp.append(review['text'])

# 	placesToSeeReviews[tempResJsonRes["place_id"]] = temp
# print("**************************************PLACES TOO SEE REVIEWS**************************************")
# print(placesToSeeReviews)
# print("**************************************PLACES TOO SEE REVIEWS**************************************")


restaurantsReviews = {}
centralRestReviews = {} 
forumRestReviews = {} 
royalRestReviews = {} 
rajajiRestReviews = {} 
indiraRestReviews = {} 

# resInJson = centralRest.json()
# centralRestRes = resInJson['results']

# for place in centralRestRes:
# 	tempRes = re.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+place['place_id']+'&key=AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY')
# 	tempResJson = tempRes.json()
# 	tempResJsonRes = tempResJson['result']

# 	temp = []
# 	for review in tempResJsonRes['reviews']:
# 		temp.append(review['text'])

# 	centralRestReviews[tempResJsonRes["place_id"]] = temp
# print("**************************************CENTRAL RESTAURANTS REVIEWS**************************************")
# print(centralRestReviews)
# print("**************************************CENTRAL RESTAURANTS REVIEWS**************************************")


# resInJson = forumRest.json()
# forumRestRes = resInJson['results']

# for place in forumRestRes:
# 	tempRes = re.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+place['place_id']+'&key=AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY')
# 	tempResJson = tempRes.json()
# 	tempResJsonRes = tempResJson['result']

# 	temp = []
# 	for review in tempResJsonRes['reviews']:
# 		temp.append(review['text'])

# 	forumRestReviews[tempResJsonRes["place_id"]] = temp
# print("**************************************FORUM RESTAURANTS REVIEWS**************************************")
# print(forumRestReviews)
# print("**************************************FORUM RESTAURANTS REVIEWS**************************************")


# resInJson = royalRest.json()
# royalRestRes = resInJson['results']

# for place in royalRestRes:
# 	tempRes = re.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+place['place_id']+'&key=AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY')
# 	tempResJson = tempRes.json()
# 	tempResJsonRes = tempResJson['result']

# 	temp = []
# 	for review in tempResJsonRes['reviews']:
# 		temp.append(review['text'])

# 	royalRestReviews[tempResJsonRes["place_id"]] = temp
# print("**************************************ROYAL MEENA RESTAURANTS REVIEWS**************************************")
# print(royalRestReviews)
# print("**************************************ROYAL MEENA RESTAURANTS REVIEWS**************************************")


# resInJson = rajajiRest.json()
# rajajiRes = resInJson['results']

# for place in rajajiRes:
# 	tempRes = re.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+place['place_id']+'&key=AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY')
# 	tempResJson = tempRes.json()
# 	tempResJsonRes = tempResJson['result']

# 	temp = []
# 	for review in tempResJsonRes['reviews']:
# 		temp.append(review['text'])

# 	rajajiRestReviews[tempResJsonRes["place_id"]] = temp
# print("**************************************RJ NAGAR RESTAURANTS REVIEWS**************************************")
# print(rajajiRestReviews)
# print("**************************************RJ NAGAR RESTAURANTS REVIEWS**************************************")


# resInJson = indiraRest.json()
# indiraRestRes = resInJson['results']
# print("LEn:",len(indiraRestRes))
# for place in indiraRestRes:
# 	tempRes = re.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+place['place_id']+'&key=AIzaSyC9veNE4mgY5zjZoT0ev2LSTWmZl8i7akY')
# 	tempResJson = tempRes.json()
# 	tempResJsonRes = tempResJson['result']

# 	temp = []
# 	for review in tempResJsonRes['reviews']:
# 		temp.append(review['text'])

# 	indiraRestReviews[tempResJsonRes["place_id"]] = temp
# print("**************************************INDIRA NAGAR RESTAURANTS REVIEWS**************************************")
# print(indiraRestReviews)
# print("**************************************INDIRA NAGAR RESTAURANTS REVIEWS**************************************")
