import os
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.txt")
print(path)

fh = open(path, "r", encoding="utf-8")

while True:
    line = fh.readline()
    if not line:
        break
    print(line, end="")

fh.close()
