msg = "hello world! hi!"
results = [value for char in msg if (value := ord(char)) >= 97 and value <= 122]
print(results)