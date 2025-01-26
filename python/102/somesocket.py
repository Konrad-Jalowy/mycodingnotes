import socket

host = "example.com"
port = 80

# Tworzenie połączenia TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    # Wysyłanie żądania HTTP
    request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    s.sendall(request.encode())

    # Odbieranie odpowiedzi
    response = b""
    while True:
        data = s.recv(1024)
        if not data:
            break
        response += data

# Wyświetlenie odpowiedzi
print(response.decode())
