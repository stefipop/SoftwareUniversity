def title(article_name):
    print(f"<h1>\n\t{article_name}\n</h1>")


def content(article_content):
    print(f"<article>\n\t{article_content}\n</article>")


def comments(paragraphs):
    print(f"<div>\n\t{paragraphs}\n</div>")


name = input()
title(name)
paragraph_name = input()
content(paragraph_name)
data = input()
while data != "end of comments":
    comments(data)
    data = input()
