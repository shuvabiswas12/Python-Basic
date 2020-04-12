"""

collections = [12, 2.4, "salt food]

    [expr for val in collections]
    [expr for val in collections if <test>]
    [expr for val in collections if <test_1> and <test_2>]
    [expr for val in collections_1 and val2 in collections2]

"""


# print 100 positive integers using list comprehension
positive_integer = [value for value in range(1, 100) if (value % 2) ==0]
print(positive_integer)


# finding the movie name that is started with 'G'
movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story", "Gone with the wind",
          "Citizen Kane", "It's a wonderful life", "The wizard of Oz", "Gattaca"]

movie_starts_with_G = [movie for movie in movies if movie.startswith("G")]
print(movie_starts_with_G)


# cartesian product
A = [2, 4, 3]
B = [9, 6, 5]

cartesian_product = []
cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)


#  printing the letter from a string
letter = [letter for letter in 'Bangladesh']
print(letter)




