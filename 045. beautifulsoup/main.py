from bs4 import BeautifulSoup

with open("./website.html", encoding="UTF-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.prettify())