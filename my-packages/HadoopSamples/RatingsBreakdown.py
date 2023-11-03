
from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):
    
    def steps_OLD(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=[self.reducer_count_ratings, self.reducer_sort_ratings])
        ]
        
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_movies, reducer=self.reducer_count_movies),
            MRStep(reducer=self.reducer_sort_movies)
        ]

    def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield rating, 1

    def reducer_count_ratings(self, key, values):
        yield key, sum(values)

    def mapper_get_movies(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1

    def reducer_count_movies(self, key, values):
        yield sum(values), key
    
    def reducer_sort_movies(self, keys, values):
        yield keys.sort()

#if __name__ == '__main__':
#    RatingsBreakdown.run()
