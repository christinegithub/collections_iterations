# Save each of the following lists and dictionaries into variables. You will use them throughout the assignment.
#
# Eg. fav_colours = ...
#
# Create a list for each item below that contains the given information:
#
# your favourite colours
# the age of you and your siblings/cousins/friends
# flip a coin 5 times and record whether or not the result was 'heads'
# your three favourite performing artists
# Create a dictionary for each item below that contains the given information:
#
# three words and their definitions
# your favourite movie names and their year of creation
# three cities of the world and their population
# the names of your siblings/cousins/friends and their ages
# After you've done that you should run your code to make sure there aren't any syntax errors.
# You should get in the habit of running your code after each step in order to catch any mistakes as soon as they're introduced.

# Exercise 0

fav_colours = ['blue', 'green', 'red', 'purple']
age = [17, 28, 30, 35]
coin_flips = ['heads', 'heads', 'tail', 'tail', 'heads']
performing_artists = ['Adam', 'Britney', 'Shakira']

definitions = {
'walk': 'slowly jog',
'jog': 'slowly run',
'run': 'quickly jog'
}

movie_and_year = {
'black panther': 2018,
'the big short': 2015,
'crazy rich asians': 2019
}

cities_and_population = {
'toronto': 2730000,
'rome': 2870000,
'manila': 1780000
}

name_and_age = {
'Sam': 20,
'Alex': 30,
'Stella': 35
}

# Exercise 1
# Print out the list of coin flips.
# Print out the first element of the list of your favourite colours.
# Output the sorted version of the list of your friends and family members' ages.
# Add a new baby (0 years old) to the list of your family's ages.
# Using the dictionary of movie information, access and print the year of one of the movies.
# If you haven't done so recently, now would be a good time to check that your code works and commit once it does.

print(coin_flips)

print(fav_colours[0])

age.sort()
print(age)

age.append(0)
print(age)

print(movie_and_year['black panther'])
