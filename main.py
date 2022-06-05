""" Main class that calls on user and preferences class. Does the overall functions finding restaurants
based on preferences, location, and user history. """
class Main:

    """ Takes in user name and top five categories. Creates user. """
    def __init__(self, name, ffive):

        nameList = name.split(" ")
        user = User(nameList[0], nameList[1], ffive)



    """ Returns a list of max 20 nearby restaurants in the area, according to user location. """
    def getRestaurants(self):
        restaurants = [] """ *** Learn how to set an endpoint here. *** """

        """ Figure how to set endpoint to retrieve list of restaurants through Yelp API. """
        return restaurants

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
