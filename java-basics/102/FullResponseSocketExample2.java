import java.net.Socket;
import java.io.OutputStream;
import java.io.InputStream;
import java.nio.charset.Charset;
import java.util.HashMap;
import java.util.Map;

public class FullResponseSocketExample2 {
    public static void main(String[] args) throws Exception {
        try (Socket socket = new Socket("example.com", 80)) {
            // Pobranie strumieni wejścia i wyjścia
            OutputStream out = socket.getOutputStream();
            InputStream in = socket.getInputStream();

            // Przygotowanie żądania HTTP
            String request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n";
            out.write(request.getBytes());
            out.flush(); // Wysłanie żądania do serwera

            // Odczyt odpowiedzi
            StringBuilder headers = new StringBuilder();
            StringBuilder body = new StringBuilder();
            Map<String, String> headerMap = new HashMap<>();
            Charset charset = Charset.defaultCharset(); // Domyślne kodowanie

            byte[] buffer = new byte[1024];
            int bytesRead;
            boolean isReadingHeaders = true;

            while ((bytesRead = in.read(buffer)) != -1) {
                String data = new String(buffer, 0, bytesRead);

                // Podziel odpowiedź na nagłówki i treść
                if (isReadingHeaders) {
                    int index = data.indexOf("\r\n\r\n");
                    if (index != -1) {
                        // Dodaj nagłówki do zmiennej
                        headers.append(data, 0, index + 4);
                        parseHeaders(headers.toString(), headerMap);

                        // Sprawdź kodowanie w nagłówkach
                        String contentType = headerMap.get("Content-Type");
                        if (contentType != null && contentType.contains("charset=")) {
                            String[] parts = contentType.split("charset=");
                            if (parts.length > 1) {
                                charset = Charset.forName(parts[1].trim());
                            }
                        }

                        // Dodaj pierwszą część ciała odpowiedzi
                        body.append(data.substring(index + 4));
                        isReadingHeaders = false;
                    } else {
                        headers.append(data);
                    }
                } else {
                    // Dodaj resztę ciała odpowiedzi
                    body.append(data);
                }
            }

            // Wyświetlenie nagłówków
            System.out.println("Nagłówki odpowiedzi:");
            System.out.println(headers);

            // Wyświetlenie treści
            System.out.println("\nTreść odpowiedzi:");
            System.out.println(body.toString().strip());

        }
    }

    private static void parseHeaders(String headers, Map<String, String> headerMap) {
        String[] lines = headers.split("\r\n");
        for (int i = 1; i < lines.length; i++) { // Pomijamy pierwszą linię statusu
            String[] parts = lines[i].split(": ", 2);
            if (parts.length == 2) {
                headerMap.put(parts[0].trim(), parts[1].trim());
            }
        }
    }
}
