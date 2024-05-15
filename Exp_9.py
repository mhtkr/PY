#Experiment - 9

import re

with open('text_file.txt', 'r') as file:
    text_data = file.read()

pattern = r'\b\w*Microsoft\w*\b'

re.findall
matches = re.findall(pattern, text_data, re.IGNORECASE)

print("Instances of the pattern 'Microsoft':", matches)
