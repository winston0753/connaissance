""" Main class that calls on user and preferences class. Does the overall functions finding restaurants
based on preferences, location, and user history. """
class Main:

    """ Takes in user name and top five categories. Creates user. """
    def __init__(self, name, ffive):

        nameList = name.split(" ")
        
        user = User(nameList[0], nameList[1], ffive)
