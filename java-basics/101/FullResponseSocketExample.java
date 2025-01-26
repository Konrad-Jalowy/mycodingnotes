import java.net.Socket;
import java.io.OutputStream;
import java.io.InputStream;

public class FullResponseSocketExample {
    public static void main(String[] args) throws Exception {
        try (Socket socket = new Socket("google.com", 80)) {
            // Pobranie strumieni wejścia i wyjścia
            OutputStream out = socket.getOutputStream();
            InputStream in = socket.getInputStream();

            // Przygotowanie żądania HTTP
            String request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n";
            out.write(request.getBytes());
            out.flush(); // Wysłanie żądania do serwera

            // Odczyt odpowiedzi
            byte[] buffer = new byte[1024]; // Bufor na porcje danych
            int bytesRead; // Liczba odczytanych bajtów

            while ((bytesRead = in.read(buffer)) != -1) {
                // Konwersja odczytanych bajtów na tekst i wypisanie
                System.out.print(new String(buffer, 0, bytesRead));
            }
        }
    }
}
