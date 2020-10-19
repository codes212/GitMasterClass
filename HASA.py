class SportsNews:
    def getSportsInfo(self):
        print('Sports Information 1')
        print('Sports Information 2')
        print('Sports Information 3')

class MovieNews:
    def getMovieInfo(self):
        print('Movie Information 1')
        print('Movie Information 2')
        print('Movie Information 3')

class PoliticsNews:
    def getPoliticsInfo(self):
        print('Politics Information 1')
        print('Politics Information 2')
        print('Politics Information 3')


class DhrumilNews:
    def __init__(self):
        self.sports = SportsNews()
        self.movie = MovieNews()
        self.politics = PoliticsNews()

    def getTotalNews(self):
        print('Welcome to total news Info')
        self.sports.getSportsInfo()
        self.movie.getMovieInfo()
        self.politics.getPoliticsInfo()

hnews = DhrumilNews()
hnews.getTotalNews()