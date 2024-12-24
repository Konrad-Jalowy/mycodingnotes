msg = "hello world"
msg_numbers = []
msg_again = ""

for letter in msg:
    print(ord(letter))
    msg_numbers.append(ord(letter))
else:
    print(msg_numbers)

for letter in msg_numbers:
    print(chr(letter))
    msg_again += chr(letter)
else:
    print(msg_again)