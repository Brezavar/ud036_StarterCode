import media
import fresh_tomatoes

#use Movie class constructor to create movie objects

toy_story = media.Movie("Toy Story - "+media.Movie.VALID_RATINGS[0],
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story2 = media.Movie("Toy Story 2 - "+media.Movie.VALID_RATINGS[0],
                         "http://www.pixartalk.com/wp-content/uploads/2009/06/ts2postertrio.jpg",
                         "https://www.youtube.com/watch?v=Lu0sotERXhI")

toy_story3 = media.Movie("Toy Story 3 - "+media.Movie.VALID_RATINGS[0],
                         "http://cdn2-www.comingsoon.net/assets/uploads/2010/04/file_65512_0_toystory3international.jpg",
                         "https://www.youtube.com/watch?v=JcpWXaA2qeg")

la_confidential = media.Movie("LA Confidential - "+media.Movie.VALID_RATINGS[3],
                              "https://images-na.ssl-images-amazon.com/images/I/51xo9dyr4TL.jpg",
                              "https://www.youtube.com/watch?v=C4XbnrmbEME")

blade_runner = media.Movie("Blade Runner - "+media.Movie.VALID_RATINGS[3],
                           "https://images-na.ssl-images-amazon.com/images/I/51ZmDpb2QfL.jpg",
                           "https://www.youtube.com/watch?v=iYhJ7Mf2Oxs")

dark_knight = media.Movie("The Dark Knight - "+media.Movie.VALID_RATINGS[2],
                          "https://images-na.ssl-images-amazon.com/images/I/81AJdOIEIhL._SY550_.jpg",
                          "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

fresh_tomatoes.open_movies_page(media.Movie.movie_instance_list)
