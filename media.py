class Movie():
    
    VALID_RATINGS = ["G","PG", "PG-13", "R"]
    
    movie_instance_list = []
    
    #create structure for movie objects passed through this init function

    def __init__(self,
                movie_title,
                poster_image,
                trailer_youtube):

        print("Movie constructor has been called")

        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        #add each movie object into array 
        Movie.movie_instance_list.append(self)

    
    
