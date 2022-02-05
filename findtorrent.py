import requests
from imdb import IMDb 


ia = IMDb()

f = open("toDownloadMovies.txt" , "r+")
movies_list = []

for x in f:
    movies_list.append(x)

movie_id= []
for i in movies_list:
    temp = ia.search_movie(i)
    temp_movieID = temp[0].movieID
    temp_movieID = "tt" + temp_movieID
    movie_id.append(temp_movieID)

print(movie_id)    

for i in range(len(movie_id)):
    print("Movie is", movies_list[i]) 
    yify_url = f"https://yts.mx/api/v2/list_movies.json?query_term={movie_id[i]}&quality=720p"
    yify_api = requests.get(yify_url)
    data = yify_api.json()['data']['movies']
    torrent = data[0]['torrents']
    link = torrent[0]['url']
    print(link)

    file = requests.get(link)
    destination = f"{movies_list[i]}.torrent"
    open(destination,'wb').write(file.content)


f.truncate(0)
f.close()



