import tkinter as tk
from tkinter import simpledialog
import socket
import threading
import json

class ChatClientGUI:
    def __init__(self):
        # Utworzenie okna GUI
        self.root = tk.Tk()
        self.root.title("Chat Client")

        # Pole do wyświetlania wiadomości
        self.chat_display = tk.Text(self.root, state="disabled", wrap="word")
        self.chat_display.pack(expand=True, fill="both", padx=10, pady=10)

        # Pole do wpisywania wiadomości
        self.entry_field = tk.Entry(self.root)
        self.entry_field.pack(fill="x", padx=10, pady=5)
        self.entry_field.bind("<Return>", self.send_message)

        # Socket klienta
        self.client_socket = None
        self.running = True

        # Inicjalizacja połączenia
        self.initialize_connection()

        # Wątek nasłuchujący
        threading.Thread(target=self.receive_messages, daemon=True).start()

        # Uruchomienie GUI
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def initialize_connection(self):
        # Nazwa użytkownika
        self.username = simpledialog.askstring("Nazwa użytkownika", "Podaj swoją nazwę użytkownika:", parent=self.root)

        if not self.username:
            self.running = False
            self.root.destroy()
            return

        # Połączenie z serwerem
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 5000))

        # Rejestracja na serwerze
        self.send_to_server({"type": "register", "username": self.username})

    def send_message(self, event=None):
        # Pobierz wiadomość z pola Entry
        message = self.entry_field.get()
        if message:
            self.update_chat(f"Ty: {message}")
            self.send_to_server({"type": "message", "content": message})
            self.entry_field.delete(0, tk.END)

    def send_to_server(self, message):
        # Serializacja i wysyłanie wiadomości do serwera
        try:
            self.client_socket.sendall(json.dumps(message).encode("utf-8"))
        except:
            self.update_chat("Błąd: Nie można wysłać wiadomości.")

    def receive_messages(self):
        # Nasłuchiwanie na wiadomości od serwera
        while self.running:
            try:
                data = self.client_socket.recv(1024).decode("utf-8")
                if data:
                    message = json.loads(data)
                    self.update_chat(f"{message['username']}: {message['content']}")
            except:
                self.update_chat("Rozłączono z serwerem.")
                self.running = False

    def update_chat(self, message):
        # Aktualizowanie pola wyświetlania wiadomości
        self.chat_display.config(state="normal")
        self.chat_display.insert("end", message + "\n")
        self.chat_display.config(state="disabled")
        self.chat_display.see("end")

    def on_close(self):
        # Zamknięcie aplikacji
        self.running = False
        self.client_socket.close()
        self.root.destroy()

if __name__ == "__main__":
    ChatClientGUI()
