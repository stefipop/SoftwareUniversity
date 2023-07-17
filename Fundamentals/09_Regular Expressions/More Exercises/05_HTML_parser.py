import re

html = input()

html = html.replace('\\n', '')
title_pattern = r"<title>(.*?)<\/title>"
title_match = re.search(title_pattern, html)
title = title_match.group(1)

print(f"Title: {title}")
html = html.replace(title, '')

content_matches = re.findall(r">(.*?)<", html)
content_cleaned = [element.strip() for element in content_matches if element.strip() != '']
content = ' '.join(content_cleaned)

print(f"Content: {content}")
