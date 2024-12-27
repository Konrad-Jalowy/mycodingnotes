with open("context.txt", mode="r") as file:
    while line := file.readline():
        print(line.rstrip())