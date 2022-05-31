"""
A user of the app. The User class stores the information of the current user, including but not limited to cuisine preferences,
restaurant history, dishes they often order, and restaurants their friends frequent.
"""
class User:

    firstName, lastName = "", ""

    #init function: takes a first and last name and sets them with the setFName and setLName functions
    def __init__(self, fname, lname):
        this.setFName(fname)
        this.setLName(lname)

    #sets the first name of the User
    def setFName(self, fname):
        firstName = fname

    #sets the last name of the User
    def setLName(self, lname):
        lastName = lname

    #returns the full name of the User
    def getFullName(self):
        return getFName() + " " + getLName()

    #returns the User's first name
    def getFName(self):
        return firstName

    #returns the User's last name
    def getLName(self):
        return lastName
