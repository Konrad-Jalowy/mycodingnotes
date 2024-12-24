import os
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.txt")
print(path)

fh = open(path, "r", encoding="utf-8")

while line := fh.readline():
    print(line, end="")
else:
    print()
    print("Finished reading")

fh.close()
