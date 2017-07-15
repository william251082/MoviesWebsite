import webbrowser

class Video():
    """This is the parent class of Movie and TV show classes."""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self, movie_title, duration):
        self.title = movie_title
        self.duration = duration

class Movie(Video):
    """This class provides a way to store a movie related information."""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    """This class provides a way to store a TV show related information."""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
