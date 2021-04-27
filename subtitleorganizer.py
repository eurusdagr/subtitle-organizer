import imdb
import os
import shutil


ia = imdb.IMDb()
directory = os.chdir(input())
for file in os.listdir(directory):
    try:
        movie = ia.search_movie(file)
        movie = movie[0].getID()
        movie = ia.get_movie(movie)
        print(movie)
    except IndexError:
        print("API didn't find anything")
    else:
        try:
            for director in movie["directors"]:

                try:
                    print(director)
                    directorname = director["name"]
                    if os.path.isdir(directorname) == True:
                        shutil.move(file, directorname)
                    else:
                        os.mkdir(director["name"])
                        shutil.move(file, directorname)
                except TypeError:
                    print("")
                    pass
        except KeyError:
            print("no information")
            pass
