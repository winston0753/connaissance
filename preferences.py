"""
Preferences class that tracks the user's preferred cuisines.
"""
class Preferences:

    "creates the user preferences list and appends the first five categories"
    def __init__(self, firstFive):
        self.preferences = []
        self.preferences.extend(firstFive)
