# your code goes here

def read_ratings(filename):
    """Returns restaurants alphabetically with rating.

    Input: file with restaurant names and ratings.
    Output: Sorted restaurant names and ratings.
    """
    opened_file = open(filename)
    restaurant_ratings = {}

    user_restaurant = raw_input("What restaurant would you like to add?: "
                                ).capitalize()
    user_rating = int(raw_input("What rating do you give the restaurant?: "))

    for line in opened_file:
        restaurant, rating = line.rstrip().split(":")
        restaurant_ratings[restaurant] = rating

    restaurant_ratings[user_restaurant] = user_rating
    restaurants_ordered = sorted(restaurant_ratings.items())
    
    for restaurant, rating in restaurants_ordered:
        print "{} is rated at {}".format(restaurant, rating)


    opened_file.close()


read_ratings("scores.txt")