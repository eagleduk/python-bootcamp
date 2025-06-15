from bs4 import BeautifulSoup

with open("./website.html", encoding="UTF-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.prettify())

print(soup.a)
print(soup.a.get("href"))
print(soup.a.getText())

first_anchor_tag = soup.find(name="a")
print(first_anchor_tag)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
for tag in all_anchor_tags:
    print(tag.getText())

all_selector_tags = soup.select(selector="a")
print(all_selector_tags)

print(soup.select_one(selector="a"))
