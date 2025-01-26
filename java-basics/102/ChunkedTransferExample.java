import java.io.InputStream;
import java.net.Socket;

public class ChunkedTransferExample {
    public static void main(String[] args) throws Exception {
        try (Socket socket = new Socket("httpbin.org", 80)) {
            // Przygotowanie strumieni wejścia i wyjścia
            InputStream in = socket.getInputStream();
            socket.getOutputStream().write("GET /stream/2 HTTP/1.1\r\nHost: httpbin.org\r\n\r\n".getBytes());

            // Odczyt nagłówków
            StringBuilder headers = new StringBuilder();
            int b;
            while ((b = in.read()) != -1) {
                headers.append((char) b);
                if (headers.toString().endsWith("\r\n\r\n")) break;
            }
            System.out.println("Nagłówki:");
            System.out.println(headers);

            // Odczyt chunked transfer encoding
            System.out.println("\nTreść:");
            while (true) {
                // Odczytaj rozmiar chunka
                StringBuilder chunkSizeHex = new StringBuilder();
                while ((b = in.read()) != -1) {
                    if (b == '\r') break; // Rozmiar kończy się przed '\r\n'
                    chunkSizeHex.append((char) b);
                }
                in.read(); // Odczytaj '\n'

                // Konwertuj rozmiar chunka z heksadecymalnego na dziesiętny
                int chunkSize = Integer.parseInt(chunkSizeHex.toString().trim(), 16);
                if (chunkSize == 0) break; // Ostatni chunk

                // Odczytaj treść chunka
                byte[] chunk = new byte[chunkSize];
                in.read(chunk);
                System.out.print(new String(chunk));

                // Odczytaj końcowe '\r\n' chunka
                in.read();
                in.read();
            }
        }
    }
}
