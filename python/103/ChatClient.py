import tkinter as tk
import socket
import threading
import json


class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Client")

        self.text_area = tk.Text(root, state='disabled', wrap='word')
        self.text_area.pack(expand=True, fill='both')

        self.entry = tk.Entry(root)
        self.entry.pack(fill='x')
        self.entry.bind('<Return>', self.send_message)

        self.connect_to_server()

    def connect_to_server(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 5000))
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self, event=None):
        message = self.entry.get()
        if message:
            json_message = json.dumps({"type": "message", "content": message})
            self.client_socket.sendall(json_message.encode('utf-8'))
            self.entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024).decode('utf-8')
                response = json.loads(data)
                self.update_chat(response["content"])
            except:
                self.update_chat("Rozłączono z serwerem.")
                break

    def update_chat(self, message):
        self.text_area.config(state='normal')
        self.text_area.insert('end', message + '\n')
        self.text_area.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()
