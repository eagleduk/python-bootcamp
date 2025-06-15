from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

all_vote_tr_tags = soup.find_all(name="tr", class_="athing")

all_ranks = []

for vote_tr_tag in all_vote_tr_tags:
    anchor = vote_tr_tag.find(name="a", class_="storylink")
    text = anchor.getText()
    href = anchor.get("href")
    id = vote_tr_tag.get("id")
    score_span = vote_tr_tag.find_next("tr").find(name="span", class_="score")
    score = score_span.getText().split(" ")[0]
    print(f"text: {text}, link: {href}, score={score}")

    all_ranks.append({
        "text": text,
        "link": href,
        "score": int(score)
    })

print(all_ranks)

sort_ranks = sorted(all_ranks, key=lambda x: x["score"], reverse=True)
print(sort_ranks)
