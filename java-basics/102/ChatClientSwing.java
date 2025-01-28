package org.example;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.net.Socket;

public class ChatClientSwing {

    private JTextArea chatArea;
    private JTextField inputField;
    private Socket socket;
    private BufferedReader reader;
    private PrintWriter writer;

    public ChatClientSwing() {
        // Tworzenie GUI
        JFrame frame = new JFrame("Chat Client");
        frame.setSize(400, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        chatArea = new JTextArea();
        chatArea.setEditable(false); // Tylko do odczytu
        chatArea.setLineWrap(true);

        JScrollPane scrollPane = new JScrollPane(chatArea);
        frame.add(scrollPane, BorderLayout.CENTER);

        inputField = new JTextField();
        frame.add(inputField, BorderLayout.SOUTH);

        // Obsługa wysyłania wiadomości
        inputField.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sendMessage();
            }
        });

        frame.setVisible(true);

        // Połączenie z serwerem
        connectToServer();
        startListening();
    }

    private void connectToServer() {
        try {
            // Adres IP i port serwera
            socket = new Socket("127.0.0.1", 5000);

            // Strumienie do komunikacji z serwerem
            reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            writer = new PrintWriter(socket.getOutputStream(), true);

            appendToChatArea("Połączono z serwerem.");
        } catch (IOException ex) {
            appendToChatArea("Błąd połączenia z serwerem: " + ex.getMessage());
        }
    }

    private void startListening() {
        Thread listeningThread = new Thread(() -> {
            try {
                String line;
                while ((line = reader.readLine()) != null) {
                    appendToChatArea(line); // Dodaj odebraną wiadomość do GUI
                }
            } catch (IOException ex) {
                appendToChatArea("Rozłączono z serwerem.");
            }
        });

        listeningThread.setDaemon(true);
        listeningThread.start();
    }

    private void sendMessage() {
        String message = inputField.getText();
        if (!message.isEmpty()) {
            writer.println(message); // Wysyłanie wiadomości do serwera
            inputField.setText(""); // Czyszczenie pola wejściowego
        }
    }

    private void appendToChatArea(String message) {
        SwingUtilities.invokeLater(() -> chatArea.append(message + "\n"));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(ChatClientSwing::new);
    }
}
