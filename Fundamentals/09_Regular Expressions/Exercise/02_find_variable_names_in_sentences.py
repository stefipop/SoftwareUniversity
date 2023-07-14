import re

text = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
found_name = re.findall(pattern, text)
print(','.join(found_name))
