
class weighted:

    def get_rating(x, C, m):
        v = x['vote_count']
        R = x['vote_average']
        rating = ((v / (v + m)) * R + (m / (v + m)) * C)
        return rating
