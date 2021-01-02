from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movie_list = [movie.getText() for movie in movies]

# print(movie_list)

reversed_movie_list = movie_list[::-1]
# print("updated list: ", reversed_movie_list)
reversed_movie_list[0] = "1) " + reversed_movie_list[0]
# print(reversed_movie_list[0])
# print("updated list: ", reversed_movie_list)

with open("movie_list.txt", mode="w") as file:
    for title in reversed_movie_list:
        file.write(f"{title}\n")
