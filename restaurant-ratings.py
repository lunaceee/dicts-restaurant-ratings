# your code goes here


restaurant_ratings = {}

def read_ratings(filename):
    opened_file = open(filename)
    for line in opened_file:
        new_line = line.rstrip()
        restaurant_and_rating = new_line.split(":")
        restaurant = restaurant_and_rating[0]
        restaurant_ratings[restaurant] = restaurant_and_rating[1]
    restaurants_ordered = sorted(restaurant_ratings.items())
    for restaurant, rating in restaurants_ordered:
        print "{} is rated at {}".format(restaurant,rating)



read_ratings("scores.txt")