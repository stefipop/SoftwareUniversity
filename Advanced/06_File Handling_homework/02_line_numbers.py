import re
from string import punctuation

with open('text.txt', 'r') as file, open('output.txt', 'w') as output_file:
    for line, text in enumerate(file):
        stripped = text.strip()
        letter_count = len(re.findall('[A-Za-z]', stripped))
        marks_count = len([char for char in stripped if char in punctuation])
        output_file.write(f'Line {line + 1}: {stripped} ({letter_count})({marks_count})\n')
