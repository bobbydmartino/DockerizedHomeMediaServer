# Dockerized Home Media Server

My family has been building a Classic Movie Collection for about 30 years now. It started with my fathers vhs collection, which he would have you know rivaled blockbuster back in the day. Later, all the movies, including the ones that were continuing to be added were converted to dvd's. This, in response to redbox. We really did hate paying for content. With the advent of streaming services, we found [plex](plex.tv) and converted the entire collection to digital streaming. Now wherever we go we can have access to movies from [Great Train Robbery](https://en.wikipedia.org/wiki/The_Great_Train_Robbery_(1903_film)) to the end of the golden age and beginnings of film noir with [rebel without a cause](https://en.wikipedia.org/wiki/Rebel_Without_a_Cause) and [psycho](https://en.wikipedia.org/wiki/Psycho_(1960_film))

## Implementation:
All of our servers run on [intel nuc's](https://www.intel.com/content/www/us/en/products/details/nuc.html). initial_install.sh merely puts dependecies for docker onto the machines when ubuntu server is first installed

startdockers.sh runs docker compose and runs plex_build. Plex_build is a container that runs the proper python code with the [plexapi library](https://github.com/pkkid/python-plexapi) in order to keep track of everything on the system, it outputs "movie_list.csv" and "tv_list.csv" along with all the metadata that plex has collected.

run.sh runs plex_build's movies.py, which outputs the csv files