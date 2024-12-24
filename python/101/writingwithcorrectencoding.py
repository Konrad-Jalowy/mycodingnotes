import os
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test2.txt")
print(path)

fh = open(path, "w", encoding="utf-8")
fh.write("hello world ąęśćżczź")
fh.close()
