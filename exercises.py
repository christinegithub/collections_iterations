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
#
# # Exercise 2
# # Print out the last element of the list of your favourite colours.
# # Note: do this in a way that would still work for a list of any size!
# # Add a new city to the dictionary of cities and population.
# # Reverse the list of coin flips and save it.
# # Print out the population of one of the cities.
# # Print out a sentence about each item in the list of performing artists. For example:
# # I think Pearl Jam is great.
# # I think Lady Gaga is great.
# # I think Pink Floyd is great.
#
print(fav_colours[-1])

cities_and_population['prague'] = 1281000
print(cities_and_population)

coin_flips.reverse()
print(coin_flips)

print(cities_and_population['manila'])

for artist in performing_artists:
    print("I think {} is great.".format(artist))
#
# # Exercise 3
# # Print out the first two performing artists in that list.
# # For each of your favourite movies, print out a sentence about when the movie was released. For example:
# # Avatar came out in 2009.
# # Mean Girls came out in 2004.
# # The Matrix came out in 1999.
# # Sort and reverse the list of ages of your family. Save it and print it to the screen.
# # See if you can sort and reverse the list on one line!
# # Add "Beauty and the Beast" movie to your dictionary of movies information, but with a twist: the movie was
# # released both in 1991 and in 2017. Print it out.
#
print(performing_artists[0])
print(performing_artists[1])

for movie, year in movie_and_year.items():
    print("{} came out in {}.".format(movie, year))

age.sort(), age.reverse()
print(age)

movie_and_year['Beauty and the Beast'] = (1991, 2017)
print(movie_and_year)
#
#
# #Exercise 4
# # Print out all of the ages of your friends/family that are less than 30 (or any number where some ages
# # will not be printed!).
# # Find and output the age of the oldest person in your friends/family list.
# # Count how many times you flipped 'heads' using the coin flips list.
# # You realize one of the performing artists in your list is no longer a favourite.
# # Remove one of them from the list.
# # Pick a city in your city population dictionary and change its population.
#
under_30 = []

for indv_age in age:
    if indv_age < 30:
        under_30.append(indv_age)
print(under_30)


print(max(age))

print(coin_flips.count('heads'))

performing_artists.pop(2)
print(performing_artists)

cities_and_population['toronto'] = 100
print(cities_and_population)
#
# #Exercise 5
# #
# # Find the sum total of the population in the dictionary of cities.
# # Using your dictionary containing the names of your family and friends with their ages,
# # print out one of two messages for each depending on their age. For example:
# # Martha is old.
# # Stewart is young.
# # Holly is young.
# # Print out the last two colours in your list of favourite colours.
# # Increase by 1 the age of everyone in your list of ages. Print it out.
# # Add two new colours to your list of favourite colours.
#
print(sum(cities_and_population.values()))

for name, age in name_and_age.items():
    if age < 25:
        print("{} is young.".format(name))
    else:
        print("{} is old.".format(name))

print(fav_colours[-1])
print(fav_colours[-2])

for i, indv_age in enumerate(age):
    age[i] = indv_age + 1
print(age)

fav_colours.append('maroon')
fav_colours.append('pink')
print(fav_colours)

# Exercise 6
# Make a new dictionary that contains a list of movies for each year.
# Each list of movies should be a list. Below is some data you can use.
#
# 1999: The Matrix, Star Wars: Episode 1, The Mummy
# 2009: Avatar, Star Trek, District 9
# 2019: How to Train Your Dragon 3, Toy Story 4, Star Wars: Episode 9
# Make a new list that contains each row of the buttons on a phone. Each row should be a list.
#
# The rows on a phone are: 1 2 3, 4 5 6, 7 8 9, * 0 #
# Make a new list that contains information about three countries.
# Each country should be a dictionary that has a name, a continent, and whether or not it is an island.
#

movies_each_year = {
1999: ['The Matrix', 'Star Wars: Episode 1', 'The Mummy'],
2009: ['Avatar', 'Star Trek', 'District 9'],
2019: ['How to Train Your Dragon 3, Toy Story 4, Star Wars: Episode 9']
}

row_phone_buttons = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
['*', 0, '#']
]

countries = [
{'name': 'canada', 'continent': 'north america', 'island': False},
{'name': 'brazil', 'continent': 'south america', 'island': False},
{'name': 'philippines', 'continent': 'asia', 'island': True}
]


# Exercise 7
# Output the message "I will not skateboard in the halls" 20 times.
#
# Create a list consisting of the above message. It should appear in the list 20 times.
#
# Create a list consisting of the numbers between 1 and 50.
#
# Use a for loop to find the sum of the numbers in the above list.
#
# Create a new list which has three of each number up to 50.
#
# Ie. [1, 1, 1, 2, 2, 2, 3, 3, 3, ... , 50, 50, 50] and so on, up to 50.
# Make a new list out all of the countries from the dictionary in Exercise 6 that are not islands.
# Print out both lists.
#
print("I will not skateboard in the halls" * 20)

skateboard_message = ["I will not skateboard in the halls."] * 20
print(skateboard_message)


list_of_nums = list(range(1, 51))
print(list_of_nums)

sum = 0

for number in list_of_nums:
    sum = sum + number
print(sum)

# Create new list which has three of each number up to 50

new_list_of_nums = sorted(list_of_nums * 3)
print(new_list_of_nums)

# List countries that are not islands

not_islands = []
islands = []

for country in countries:
    if country['island']:
        islands.append(country['name'])
    elif not country['island']:
        not_islands.append(country['name'])

print(not_islands)


# Exercise 8
# You want to add up your expenses for the year.
# Create a list of numbers (integers or floats) that represents your expenses, eg:
#
# [250, 7.95, 30.95, 16.50]
#
# Add up the numbers and output the result.
#
# Put this code into a method. The method should take a list as an argument
# and return the sum of the expenses in the list. Call the method twice with different lists.


expenses_2017 = [250, 7.95, 30.95, 16.50]
expenses_2018 = [300, 30.50, 87.73, 90.30]

def sum_expenses(expense_list):
    expense_total = 0
    for expense in expense_list:
        expense_total += expense
    return expense_total

print('The total of expenses 2017 is ${:.2f}.'.format(sum_expenses(expenses_2017)))

print("The total expenses of 2018 is ${:.2f}.".format(sum_expenses(expenses_2018)))



#
#
#
#
#
#
#
