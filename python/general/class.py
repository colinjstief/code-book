
##############
## Classes

## User class
## Reference:
## https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
class User:
    """Creates a new user instance"""
    def __init__(self, name, movies):
        self.name = name
        self.movies = []

    def __repr__(self):
        return '<User {}'.format(self.name)

    def watched_movies(self):
        """Give list of watched movies"""
        return list(filter(lambda movie: movie.watched, self.movies))

    def printname(self):
        """Print user name"""
        print(self.name)

    @classmethod
    def fromjson(cls, jsonobject):
        """Create new user from json"""

        movies = []
        for movie in jsonobject['movies']:
            movies.append(Movie.fromjson(movie))

        user = cls(jsonobject['name'], movies)

        return user

## Movie class
class Movie:
    """Creates a new movie instance"""
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return '<Movie {}'.format(self.name)

    def json(self):
        """Return this class instance as a json object"""
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    @classmethod
    def fromjson(cls, jsonobject):
        """Create new user from json"""
        return cls(jsonobject['name'], jsonobject['genre'], jsonobject['watched'])
        # alternative with named arguments --> return cls( genre=jsonobject['genre'], watched = jsonobject['watched'], name = jsonobject['name'])
        # alternative with json object that matches keys --> return cls(**jsonobject)
