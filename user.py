"""
A user of the app. The User class stores the information of the current user, including but not limited to cuisine preferences,
restaurant history, dishes they often order, and restaurants their friends frequent.
"""
class User:

    """ Init function: takes fname and lnames as arguments, sets first and last names. """
    """ Takes five argument list, specifying the first five categories of restaurants that the user prefers. """
    def __init__(self, fname, lname, five):
        self.firstName = fname
        self.lastName = lname

        """ Create preferences object for user. """
        self.pref = Preferences(five)

        """ Create restaurant history of user, capping at last 100 restaurants. """
        self.userHistory = []

    """ Adds a restaurant to the user's history. If doing so exceeds history limit of 20 restaurants, remove oldest restaurant. """
    def addRestaurantHistory(self, restaurant):
        if len(self.userHistory) >= 20:
            self.userHistory.pop(0)
        self.userHistory.append(restaurant)

    def getRestaurantHistory(self):
        return self.userHistory

    """ Returns the full name of the User. """
    def getFullName(self):
        return getFName() + " " + getLName()

    def getFName(self):
        return firstName

    def getLName(self):
        return lastName
