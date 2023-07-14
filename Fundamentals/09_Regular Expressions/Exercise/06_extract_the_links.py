import re

pattern = r"(w{3}\.[a-zA-Z0-9-\.]+\.[a-z]+)"
line = input()
valid_url = []

while line:
    matches = re.search(pattern, line)
    if matches:
        valid_url.append(matches.group(1))
    line = input()

for url in valid_url:
    print(url)
