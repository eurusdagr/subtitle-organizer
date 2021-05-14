import imdb
import os
import shutil

ia = imdb.IMDb()
directory = os.chdir(input())
for file in os.listdir(directory):
    if os.path.isdir(file) == True:
        pass

    else:
        try:
            movie = ia.search_movie(file)
            selected_movie = movie[0]
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
                        else:
                            os.mkdir(director["name"])
                            shutil.move(file, directorname)
                    except TypeError:
                        print("")
                        pass
                    except shutil.Error:

                        pass
                    except FileNotFoundError:
                        pass

            except KeyError:
                print("no information")
                pass
