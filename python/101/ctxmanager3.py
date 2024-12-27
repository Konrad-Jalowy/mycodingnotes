with open("context.txt") as in_file, open("output.txt", "a") as out_file:
    while line := in_file.readline():
        out_file.write(line)