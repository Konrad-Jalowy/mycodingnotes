import socket

def main():
    # Połączenie z serwerem HTTP (przykład domeny testowej)
    with socket.create_connection(("example.com", 80)) as sock:
        # Przygotowanie żądania HTTP
        request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
        sock.sendall(request.encode("utf-8"))  # Wysyłanie żądania

        # Odczyt odpowiedzi
        response = b""
        buffer_size = 1024
        while True:
            chunk = sock.recv(buffer_size)  # Odczyt porcji danych
            if not chunk:  # Jeśli brak danych, zakończ
                break
            response += chunk

        # Wyświetlenie całej odpowiedzi jako tekst
        print(response.decode("utf-8", errors="replace"))

if __name__ == "__main__":
    main()
