import datetime
import pandas as pd
import numpy as np
from plexapi.myplex import MyPlexAccount


if __name__=="__main__":
    account = MyPlexAccount('email', 'password')
    plex = account.resource('HMS_name').connect()
    movies = plex.library.section('Movies')
    movie_list = movies.search()
    entries = []
    tvshows = plex.library.section('TV Shows')
    tvlist = tvshows.search()
    tventries = []

    for movie in tvlist:
        title = movie.title
        actors = ", ".join([x.tag for x in movie.actors[:5]])
        if movie.rating is not None:
            critic_score = int(movie.rating) * 10
        else:
            critic_score = "None"
        numseasons = len(movie.seasons())
        numepisodes = len(movie.episodes())

        if len(movie.genres) > 0:
            primary_genre = movie.genres[0].tag
            other_genres = ", ".join([x.tag for x in movie.genres[1:4]])
        else:
            primary_genre = ""
            other_genres = ""
        studio = movie.studio
        year = movie.year
        summary = movie.summary
        entry = [title,year,numseasons,numepisodes,actors,primary_genre,other_genres,studio,critic_score,summary]
        tventries.append(entry)
    print("DONE")
    columns = ['Title','Year','Num Seasons','Num Episodes','Actors','Primary Genre','Other Genres','Studio','Rating','Summary']
    df = pd.DataFrame(tventries,columns = columns)
    df.to_csv("/opt/TV_list.csv",index=False)


    for movie in movie_list:
        title = movie.title
        actors = ", ".join([x.tag for x in movie.actors[:5]])
        if movie.audienceRating is not None and movie.rating is not None:
            audience_score = int(movie.audienceRating)*10
            critic_score = int(movie.rating) * 10
        else:
            audience_score = "None"
            critic_score = "None"
        content_rating = movie.contentRating
        if len(movie.directors) > 0:
            director = movie.directors[0].tag
        else:
            director = ""
        duration = datetime.timedelta(milliseconds=movie.duration).seconds//60
        if len(movie.genres) > 0:
            primary_genre = movie.genres[0].tag
            other_genres = ", ".join([x.tag for x in movie.genres[1:4]])
        else:
            primary_genre = ""
            other_genres = ""
        studio = movie.studio

        if len(movie.producers) > 0 and len(movie.writers) > 0:
            producers = ", ".join([x.tag for x in movie.producers[:2]])
            writers = ", ".join([x.tag for x in movie.writers[:2]])
        else:
            producers = ""
            writers = ""
        year = movie.year
        summary = movie.summary
        entry = [year,duration,title,critic_score,audience_score,primary_genre,other_genres,director,actors,content_rating,summary,producers,writers,studio]
        entries.append(entry)
    print("DONE")
    columns = ["Year","Duration","Title","RT Critic Score", "RT Audience Score", "Primary Genre", "Other Genres", "Director","Actors","Content Rating", "Summary","Producers","Writers","Studio"]
    df = pd.DataFrame(entries,columns = columns)
    df.to_csv("/opt/Movie_list.csv",index=False)
