import os
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test2.txt")
print(path)

fh = open(path, "r", encoding="utf-8")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line.rstrip("\n"))