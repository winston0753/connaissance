"""
A user of the app. The User class stores the information of the current user, including but not limited to cuisine preferences,
restaurant history, dishes they often order, and restaurants their friends frequent.
"""
class User:

    "init function: takes fname and lnames as arguments, sets first and last names"
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    "returns the full name of the User"
    def getFullName(self):
        return getFName() + " " + getLName()

    "returns the User's first name"
    def getFName(self):
        return firstName

    "returns the User's last name"
    def getLName(self):
        return lastName
