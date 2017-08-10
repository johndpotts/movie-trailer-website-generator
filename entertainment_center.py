import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story")
avatar = media.Movie("Avatar")
patriot = media.Movie("The Patriot")
independance_day = media.Movie("Independance Day")
gladiator = media.Movie("Gladiator")
braveheart = media.Movie("Braveheart")



movies = [toy_story, patriot, independance_day, gladiator, braveheart, avatar]



fresh_tomatoes.open_movies_page(movies)
