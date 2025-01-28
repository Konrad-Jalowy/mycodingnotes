import asyncio


async def handle_client():
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 5000

    reader, writer = await asyncio.open_connection(SERVER_IP, SERVER_PORT)
    print(f"Połączono z serwerem {SERVER_IP}:{SERVER_PORT}")

    try:
        while True:
            # Pobierz wiadomość od użytkownika
            message = input("Wpisz wiadomość (lub 'exit' aby zakończyć): ")

            # Wyjście z programu
            if message.lower() == "exit":
                print("Zamykanie połączenia...")
                break

            # Wyślij wiadomość do serwera
            writer.write((message + "\n").encode('ascii'))
            await writer.drain()

            # Odczytaj odpowiedź od serwera
            response = await reader.read(1024)
            print(f"Odpowiedź serwera: {response.decode('ascii').strip()}")

    except Exception as e:
        print(f"Błąd: {e}")
    finally:
        writer.close()
        await writer.wait_closed()
        print("Rozłączono z serwerem.")


if __name__ == "__main__":
    asyncio.run(handle_client())
