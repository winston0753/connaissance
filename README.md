# Connaissance

Connaissance is an application that utilizes user location to determine nearby food options. From someone who is often
indecisive about what they want to eat, I find myself needing a second opinion for what's for dinner. This Connaissance
application will take user preferences, profile, past choices, and location to help narrow nearby options. The primary goal
of this application is to allow users to find suitable food choices in unfamiliar locations.

The Connaissance applications includes the Preferences, Main, and User classes. The Main class utilizes the User class object to track the user's restaurant history, as well as selected preferences. The Preferences class object is therefore used within the User class to track the individual's personal restaurant preferences.

## Preferences

The Preferences class is a simple class that stores the categorical preferences of the user in a set. The Preferences class does not store more than 10 categories at a time, and randomly removes a present category should a new entry exceed the limit.

## User

The User class is another simple class that includes the basic information of the User. This includes their name, preferences, and, more importantly, restaurant history. The 
