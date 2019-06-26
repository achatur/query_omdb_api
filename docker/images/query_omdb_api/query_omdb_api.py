import requests

class OMDB:
    def __init__(self):
        """
        Nothing to Initilize
        """

    def get_movie_from_title(self, title):
        """

        :param title:
        :return: json of movie
        """
        key = self.get_key()
        movie = requests.get("http://www.omdbapi.com/?t={}&apikey={}".format(title, key))
        return movie.json()

    def get_key(self):
        """

        :return: text api key
        """
        return ''


if "__main__" in __name__:
    """
    Main function to call OMDB
    """
    api = OMDB()

    title = input("Please Enter Movie Title: ")
    movie_json = api.get_movie_from_title(title)

    if movie_json["Response"] != "False":
        try:
            ratings = movie_json['Ratings']
            for source in ratings:
                if source['Source'] == "Rotten Tomatoes":
                    print("Movie: {}, Rotten Tomatoes Rating: {}".format(title, source['Value']))
        except Exception as e:
            print("Exception Caught {}".format(e))

    elif movie_json["Error"] == "No API key provided.":
        print("{}".format(movie_json["Error"]))

    else:
        print("Movie not Found")
