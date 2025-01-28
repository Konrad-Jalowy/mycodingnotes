import com.google.gson.Gson;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;

public class ChatClientSwing2 {

    private JTextArea chatArea;
    private JTextField inputField;
    private Socket socket;
    private InputStream inputStream;
    private PrintWriter writer;
    private Gson gson;

    public ChatClientSwing2() {
        gson = new Gson(); // Inicjalizacja Gson

        // Tworzenie GUI
        JFrame frame = new JFrame("Chat Client");
        frame.setSize(400, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        chatArea = new JTextArea();
        chatArea.setEditable(false); // Pole tekstowe tylko do odczytu
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
            // Połączenie z serwerem
            socket = new Socket("127.0.0.1", 5000);

            // Strumienie do komunikacji
            inputStream = socket.getInputStream();
            writer = new PrintWriter(socket.getOutputStream(), true);

            appendToChatArea("Połączono z serwerem.");
        } catch (IOException ex) {
            appendToChatArea("Błąd połączenia z serwerem: " + ex.getMessage());
        }
    }

    private void startListening() {
        Thread listeningThread = new Thread(() -> {
            try {
                // Bufor do odczytu danych
                byte[] buffer = new byte[1024];
                int bytesRead;

                StringBuilder messageBuilder = new StringBuilder();

                while ((bytesRead = inputStream.read(buffer)) != -1) {
                    // Odczyt danych do bufora
                    String chunk = new String(buffer, 0, bytesRead, "UTF-8");
                    messageBuilder.append(chunk);

                    // Próbujemy parsować jako JSON
                    while (true) {
                        String jsonMessage = extractJsonMessage(messageBuilder);
                        if (jsonMessage == null) break;

                        processMessage(jsonMessage);
                    }
                }
            } catch (IOException ex) {
                appendToChatArea("Rozłączono z serwerem.");
            }
        });

        listeningThread.setDaemon(true);
        listeningThread.start();
    }

    private String extractJsonMessage(StringBuilder messageBuilder) {
        String fullMessage = messageBuilder.toString();

        // Spróbuj znaleźć kompletny JSON
        int start = fullMessage.indexOf("{");
        int end = fullMessage.indexOf("}");

        if (start != -1 && end != -1 && end > start) {
            // Znaleziono kompletny JSON
            String jsonMessage = fullMessage.substring(start, end + 1);

            // Usuń przetworzoną część z buildera
            messageBuilder.delete(0, end + 1);

            return jsonMessage;
        }

        // Nie znaleziono kompletnego JSON-a
        return null;
    }

    private void processMessage(String json) {
        try {
            // Parsowanie JSON
            Map<String, String> message = gson.fromJson(json, Map.class);

            // Pobieranie zawartości wiadomości
            if (message.containsKey("content")) {
                String content = message.get("content");
                appendToChatArea("Serwer: " + content);
            } else {
                appendToChatArea("Otrzymano niepełną wiadomość: " + json);
            }
        } catch (Exception e) {
            appendToChatArea("Błąd odczytu wiadomości: " + e.getMessage());
        }
    }

    private void sendMessage() {
        String message = inputField.getText();
        if (!message.isEmpty()) {
            // Tworzenie wiadomości JSON
            Map<String, String> jsonMessage = new HashMap<>();
            jsonMessage.put("type", "message");
            jsonMessage.put("content", message);

            // Serializacja do JSON
            String json = gson.toJson(jsonMessage);

            // Wysyłanie wiadomości
            writer.println(json);
            inputField.setText(""); // Czyszczenie pola wejściowego
        }
    }

    private void appendToChatArea(String message) {
        SwingUtilities.invokeLater(() -> chatArea.append(message + "\n"));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(ChatClientSwing2::new);
    }
}
