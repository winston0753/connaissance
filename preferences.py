""" Preferences class that tracks the user's preferred cuisines. """
class Preferences:

    """ Creates the user preferences list and appends the first five categories. """
    def __init__(self, firstFive):
        self.preferences = firstFive

    def getPreferences(self):
        return self.preferences

    def addPreference(self, category):
        """ If User has 10 Preferences, then randomly remove a preference from the set and append the new category. """
        self.prefernces.append(category)
