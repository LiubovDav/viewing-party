# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}

    if title == None or title == "" or genre == None or genre == "" or rating == None or rating == "":
        return None

    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):

    watchlist = user_data["watchlist"]

    for movie in watchlist:
        if movie["title"] == title:
            watchlist.remove(movie)
            user_data["watched"].append(movie)
            return user_data
    
    return user_data
    

# user_data = {
#     "watchlist": [
#                     {
#                         "title": "Title A",
#                         "genre": "Horror",
#                         "rating": 3.5
#                     }, 
#                     {
#                         "title": "Title A",
#                         "genre": "Horror",
#                         "rating": 3.5
#                     }
#                 ],
#     "watched": [
#                     {
#                         "title": "Title A",
#                         "genre": "Horror",
#                         "rating": 3.5
#                     }, 
#                     {
#                         "title": "Title A",
#                         "genre": "Horror",
#                         "rating": 3.5
#                     }
#                 ]
# }




    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

