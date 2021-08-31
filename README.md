# Dockerized Home Media Server

My family has been building a Classic Movie Collection for about 30 years now. It started with my fathers VHS collection, which, he would have you know, rivaled blockbuster back in the day. 

As the days of tapes and rewinding came to a close, all the movies, including the ones that were continuing to be added, were converted to dvd's. This seemed to perfectly correspond to the rise of redbox.

Then, with the advent of the [plethora of streaming services](https://www.youtube.com/watch?v=TQLlnXc5Muc&t=24s), we found [plex](plex.tv) for maintaing and watching our collection and converted all the movies for digital streaming. Now wherever we go we can have access to movies from [Great Train Robbery](https://en.wikipedia.org/wiki/The_Great_Train_Robbery_(1903_film)) all the way to the end of the Golden Age and beginnings of film noir with movies such as [Rebel Without a Cause](https://en.wikipedia.org/wiki/Rebel_Without_a_Cause) and [Psycho](https://en.wikipedia.org/wiki/Psycho_(1960_film))

## Implementation:
All of our servers run on [intel nuc's](https://www.intel.com/content/www/us/en/products/details/nuc.html). initial_install.sh merely puts dependecies for docker onto the machines when ubuntu server is first installed

startdockers.sh runs docker compose and runs plex_build. Plex_build is a container that runs the proper python code with the [plexapi library](https://github.com/pkkid/python-plexapi) in order to keep track of everything on the system, it outputs "movie_list.csv" and "tv_list.csv" along with all the metadata that plex has collected.

run.sh runs plex_build's movies.py, which outputs the csv files