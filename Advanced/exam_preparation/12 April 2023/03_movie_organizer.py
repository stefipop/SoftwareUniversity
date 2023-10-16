from collections import defaultdict
def movie_organizer(*args):
    collection = defaultdict(list)
    for i in range(len(args)):
        movie_name, genre = args[i]
        collection[genre].append(movie_name)

    sorted_movie = sorted(collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""

    for genre, movies in sorted_movie:
        result += f"{genre} - {len(movies)}\n"
        for movie in sorted(movies):
            result += f"* {movie}\n"

    return result


# print(movie_organizer(
#     ("The Matrix", "Sci-fi")))
#
# print(movie_organizer(
#     ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))
#
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))