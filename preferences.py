"""
Preferences class that tracks the user's preferred cuisines.
"""
class Preferences:

    categories = {"Chinese", "Mexican", "Fast Food", "Sandwiches", "Burgers", "Noodles", "Breakfast & Brunch", "Seafood", "Japanese",
    "Pizza", "Nightlife", "Vietnamese", "Bars", "Coffee & Tea", "Chicken Wings", "Asian Fusion", "American (Traditional)", "Barbeque",
	"Tacos", "Taiwanese", "Sushi Bars", "Cafes", "Salad", "American (New)", "Cantonese", "Food Trucks", "Hot Pot", "Chicken Shop",
    "Dim Sum", "Food Delivery Services", "Soup", "Italian", "Korean", "Bakeries", "Thai", "Food Stands", "Juice Bars & Smoothies",
    "Mediterranean", "Desserts", "Szechuan", "Delis", "Specialty Food", "Hot Dogs", "Ramen", "Bubble Tea", "Cocktail Bars"
	Event Planning & Services
	Diners
	Donuts
	Vegetarian
	Latin American
	Indian
	Comfort Food
	Halal
	Caterers
	Hong Kong Style Cafe
	Middle Eastern
	Steakhouses
	Grocery
	Hawaiian
	Ice Cream & Frozen Yogurt
	Shanghainese
	Sports Bars
	Vegan
	Cajun/Creole
	Buffets
	Salvadoran
	Fish & Chips
	Street Vendors
	Wine Bars
	Beer Bar
	French
	Greek
	International Grocery
	Shaved Ice
	Arts & Entertainment
	Indonesian
	Lounges
	Meat Shops
	Poke
	Creperies
	Shopping
	Tea Rooms
	Waffles
	Cafeteria
	Empanadas
	Japanese Curry
	Pubs
	Singaporean}
    def __init__(self, firstFive):
