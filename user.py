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

    """ Returns the full name of the User. """
    def getFullName(self):
        return getFName() + " " + getLName()

    """ Returns the User's first name. """
    def getFName(self):
        return firstName

    """ Returns the User's last name. """
    def getLName(self):
        return lastName
