import re

# Wzorzec: Pliki NIE poprzedzone "ignore:"
pattern = r'(?<!ignore:)\b\w+\.\w+\b'
text = "file1.txt ignore:file2.txt file3.png"

matches = re.findall(pattern, text)
print(matches)  # Output: ['file1.txt', 'file3.png']