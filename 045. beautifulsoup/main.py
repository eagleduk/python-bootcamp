from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(selector=".content_content__i0P3p h2 strong")

ranks = [strong.getText() for strong in titles]

with open("moves.txt", "+w", encoding="UTF-8") as file:
    for rank in reversed(ranks):
        file.write(rank + "\n")
