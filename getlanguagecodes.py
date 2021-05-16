import imdb
def getlanguagecodes(self):
 ia = imdb.IMDb()
 m = ia.get_movie(ia.search_movie(self)[0].getID())
 print(m["language codes"])
getlanguagecodes(input())