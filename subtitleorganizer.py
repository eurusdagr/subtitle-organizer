import imdb
import os
import shutil
import re

ia = imdb.IMDb()
directory = os.chdir(input())
for file in os.listdir(directory):
    if os.path.isdir(file) == True:
        pass

    else:
        try:
            file1 = os.path.splitext(file)[0]
            movie = ia.search_movie(file1)
            selected_movie = movie[0]
            print(file1)
            for m in movie:
                movie = m.getID()
                movie = ia.get_movie(movie)
                if "ja" in movie.get(("language codes",)[0]):
                    selected_movie = m
                    break

            movie = selected_movie.getID()
            movie = ia.get_movie(movie)
        except IndexError:
            print("API didn't find anything")
            pass
        except TypeError:
            print("Movie in that language wasn't found")
        else:
            try:
                for director in movie["directors"]:

                    try:
                        print(director)
                        directorname = director["name"]
                        if os.path.isdir(directorname) == True:
                            shutil.move(file, directorname)
                            print("copied",file, "to the ", directorname, "folder")
                        else:
                            os.mkdir(director["name"])
                            shutil.move(file, directorname)
                            print("created the",directorname,"folder and copied",file,"to it")
                    except TypeError:
                        print("")
                        pass
                    except shutil.Error:
                        print("fould duplacete,deleting it...")
                        os.remove(file)

                        pass
                    except FileNotFoundError:
                        pass

            except KeyError:
                print("no information")
                pass
