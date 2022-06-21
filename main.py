import json
import requests
import os

import user
from user import User

"""" Taken from Yelp Fusion's documentation:
All Yelp Fusion API endpoints are under https://api.yelp.com/v3. Below are Yelp Fusion's current endpoints. """"


YELP_API = "https://api.yelp.com/v3"
BUSINESS_SEARCH = "/businesses/search"
BUSINESS_DETAILS = "/businesses" # End with business ID to get specific business details

GEOLOCATION_REQUEST = "https://www.googleapis.com/geolocation/v1/geolocate?key=" # Must end with Application API Key


""" Main class that calls on user and preferences class. Does the overall functions finding restaurants
based on preferences, location, and user history. """
class Main:

    """ Takes in user name and top five categories. Creates user.
    Creates userFile text file to persist user preferences and history. """
    def __init__(self, name, ffive):

        self.nameList = name.split(" ")
        self.user = User(self.nameList[0], self.nameList[1], ffive)
        self.userFile = open("userFile.txt", "w")
        self.userFile.write(user)
        self.userFile.close()


    """ Returns a list of max 20 nearby restaurants in the area, according to user location. """
    def getRestaurants(self):
        self.restaurants = [] """ *** Learn how to set an endpoint here. *** """

        """ Figure how to set endpoint to retrieve list of restaurants through Yelp API. """
        return self.restaurants


    """ Asks the user what kind of cuisine they are feeling. Retrieves the user's restaurant history, and, using the recent
    trends in the user's eatery history, finds a restaurant also aligns with the user's 'preferred' subcategories. Algorithm
    takes the nearby restaurants using the getRestaurants() function, filtering through the restaurants that are of the given
    category. Then uses the lists of subcategories (outdoor seating, good for kids, dinner) for those restaurants to find recurrent
    subcategories to narrow down a restaurant that is of the given category, but also suitable. """
    """ *** If ask algorithm is unable to find a restaurant within 20 miles that is of the given category, ask user to select another
    cateogory. *** """
    """ *** Else if ask yields more than one selection of the given category, find subcategories that are not overlap between remaining
    selections and ask user to pick between non-overlapping subcategories. *** """
    def ask(self, category):
        self.user = open("userFile.txt", "w")
        userHistory = self.user.getRestaurantHistory()

        preferredSubs = {} # Use Yelp endpoint to get the five most prevalent subcategories in the restaurants of userHistory
        # Getting preferredSubs likely uses multiple lines

        """ Use Geolocation API to obtain user location, and then use location to get the nearest 20 restaurants from the Yelp
        Fusion API. If there is no restaurants within the 20 of the given category, prompt user to select another category.
        Otherwise, begin narrowing down restaurants of the given category to those that have at least 2 preferredSubs. If more
        than one restaurant option remain, continue filtering restaurants by increasing the number of subcategories required from
        preferredSubs set. """
        nearestRestaurants = self.getRestaurants()
        numSubs = 2
        while nearestRestaurants:
            if " Has less than numSubs ":
                nearestRestaurants.remove("restaurant")


    """ Returns the current latitude and longitude of the user using the Geolocation API. The GET request body must be of
    JSON format. If request body is not provided, then defaults to using IP address of request location. """
    def getLocation(self):

        request = {} # Make POST request
        response = request.json()
        return response["location"]
