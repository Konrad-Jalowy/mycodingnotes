import os
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.txt")
print(path)

fh = open(path, "w")
fh.write("hello world 1")
fh.write("hello world 2")
fh.close()

fh = open(path, "a")
fh.write("hello world 3")
fh.close()