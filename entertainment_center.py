import movie
import fresh_tomatoes

hp72 = movie.Movie("Harry Potter and the Deathly Hallows Part 2",
                        "The final chapter in the Harry Potter Saga",
                        "http://movz.com/wp-content/uploads/2015/04/7xmtxRc9nQnCuWINuTT4SMP5NJc.jpg",
                        "https://www.youtube.com/watch?v=5NYt1qirBWg")
#print(hp72.storyline)

hp71 = movie.Movie("Harry Potter and the Deathly Hallows Part 1",
                   "Harry and his friends are set out to find the horcrux",
                   "http://cdn.collider.com/wp-content/uploads/harry_potter_and_the_deathly_hallows_part_1_movie_poster_heromine_harry_01.jpg",
                   "https://www.youtube.com/watch?v=Su1LOpjvdZ4")
#print(hp71.storyline)
#hp71.show_trailer()

hp7 = movie.Movie("Harry Potter and the Deathly Hallows",
                   "It's world war in the wizarding world",
                   "https://kaiserem.files.wordpress.com/2010/07/first-teaser-poster-dh.jpg",
                   "https://www.youtube.com/watch?v=9hXH0Ackz6w")

hp6 = movie.Movie("Harry Potter and the Half Blood Prince",
                   "Harry learns about dark secrets and struggles with teenage love",
                   "https://fanart.tv/fanart/movies/767/movieposter/harry-potter-and-the-half-blood-prince-555e48bd050ae.jpg",
                   "https://www.youtube.com/watch?v=JYLdTuL9Wjw")

hp5 = movie.Movie("Harry Potter and the Order of the Phoenix",
                   "Harry fights dolores Umbridge and finds out about the prophecy",
                   "http://www.tribute.ca/harrypotter/images/HP5/harry_potter_and_the_order_of_the_phoenix_poster2.jpg",
                   "https://www.youtube.com/watch?v=y6ZW7KXaXYk")

hp4 = movie.Movie("Harry Potter and the Goblet of Fire",
                   "Harry takes part in the triwizard tournament and finds out that voldermort is back",
                   "http://moviefiles.alphacoders.com/625/poster-625.jpg",
                   "https://www.youtube.com/watch?v=PFWAOnvMd1Q")

movies=[hp72, hp71, hp7, hp6, hp5, hp4]
fresh_tomatoes.open_movies_page(movies)
