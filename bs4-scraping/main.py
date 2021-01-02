from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)
# print(article_texts)
# print(article_links)

# article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
highest_upvote = max(article_upvotes)
highest_upvote_index = article_upvotes.index(highest_upvote)

print(article_texts[highest_upvote_index])
print(article_links[highest_upvote_index])
print(article_upvotes[highest_upvote_index])
# print(article_upvotes_points)
# print(article_upvotes_points.index(highest_upvote))




# article_upvotes_tag = soup.find_all(name="span", class_="score")
# article_upvotes = []
# for article in article_upvotes_tag:
#     article_upvote = article.getText()
#     article_upvotes.append(article_upvote)
# print(article_upvotes)


# story_titles = soup.find_all(name="a", class_="storylink")
# # print(story_titles)
#
# for story_title in story_titles:
#     print(story_title.getText())







# # import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#     # print(contents)
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
#
# for tag in all_anchor_tags:
#     # tag.getText()
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.get("class"))
#
# name = soup.select_one(selector="p a")
# print(name)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)