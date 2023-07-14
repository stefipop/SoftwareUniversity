import re

text = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
emails = re.findall(pattern, text)
for mail in emails:
    print(mail[0])
