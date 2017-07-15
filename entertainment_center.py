import fresh_tomatoes
import media

# Miles Ahead
miles_ahead = media.Video("Miles Ahead", "1h 40m")
miles_ahead = media.Movie(
    "Miles Ahead",
    "His story - with a little improvisation.",
    "http://i664.photobucket.com/albums/vv2/william251082/miles-ahead-poster-3_2.jpg",  # noqa
    "https://www.youtube.com/watch?v=ssfTNCTVT5U")

# Infinity
infinity = media.Video("Infinity", "1h 40m")
infinity = media.Movie(
    "Infinity",
    "Great knowledge comes from the humblest of origins.",
    "http://i664.photobucket.com/albums/vv2/william251082/dbchuhpp.jpg",
    "https://www.youtube.com/watch?v=oXGm9Vlfx4w")

# The Imitation Game
the_imitation_game = media.Video("The Imitation Game", "1h 40m")
the_imitation_game = media.Movie(
    "The Imitation Game",
    "Behind every code is an enigma.",
    "http://i664.photobucket.com/albums/vv2/william251082/Blog-photo-1.jpg",
    "https://www.youtube.com/watch?v=5gcyB72nFmc")

# Beautiful Mind
beautiful_mind = media.Video("Beautiful Mind", "1h 40m")
beautiful_mind = media.Movie(
    "Beautiful Mind",
    "He saw the world in a way no one could've imagined",
    "http://i664.photobucket.com/albums/vv2/william251082/large_v1WdKm9qQPBfhoHanBP5XxzIBDU.jpg",  # noqa
    "https://www.youtube.com/watch?v=nIR3wj9Ssaw")

# Born to be Blue
born_to_be_blue = media.Video("Born to be Blue", "1h 40m")
born_to_be_blue = media.Movie(
    "Born to be Blue",
    "A re-imagining of legend Chet Baker's musical comeback in the late '60s.",
    "http://i664.photobucket.com/albums/vv2/william251082/born-to-be-blue.jpg",
    "https://www.youtube.com/watch?v=lC1DQ9qIECo")

# Theory of Everything
theory_of_everything = media.Video("Theory of Everything", "1h 40m")
theory_of_everything = media.Movie(
    "Theory of Everything",
    "A story between the famous physicist Stephen Hawking and his wife.",
    "http://i664.photobucket.com/albums/vv2/william251082/The-Theory-Of-Everything-Movie-Poster-15-Living-Stories.jpg",  # noqa
    "https://www.youtube.com/watch?v=t-v1_OttK4A")

# Build website
movies = [miles_ahead, infinity, the_imitation_game,
          beautiful_mind, born_to_be_blue, theory_of_everything]

fresh_tomatoes.open_movies_page(movies)

# print(infinity.storyline)
# infinity.show_trailer()


# print (media.Movie.VALID_RATINGS)
print(media.Movie.__module__)
print(media.Movie.__name__)
print(media.Movie.__doc__)
