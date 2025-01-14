import re

# Wzorzec: Pliki, które NIE kończą się na ".exe"
pattern = r'\b\w+\.(?!exe)\w+\b'
text = "file1.txt file2.exe file3.jpg file4.exe file5.png"

matches = re.findall(pattern, text)
print(matches)  # Output: ['file1.txt', 'file3.jpg', 'file5.png']