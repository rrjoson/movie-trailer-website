from fresh_tomatoes import open_movies_page
from media import Movie

# List of movies
movies_list = [
    "Tarzan",
    "Spirited Away",
    "Howl's Moving Castle",
    "Pokemon",
    "World of Warcraft",
    "Eye in the sky"]

movies = []

# Store an instance of each movie in a list
i = 0
while i < len(movies_list):
	movies.append(Movie(movies_list[i]))
	i += 1

# Creates an HTML file
open_movies_page(movies)
