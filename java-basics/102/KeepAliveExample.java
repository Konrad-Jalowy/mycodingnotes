import java.net.Socket;
import java.io.OutputStream;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;

public class KeepAliveExample {
    public static void main(String[] args) throws Exception {
        try (Socket socket = new Socket("httpbin.org", 80)) {
            OutputStream out = socket.getOutputStream();
            InputStream in = socket.getInputStream();

            // Pierwsze żądanie
            String request1 = "GET /get HTTP/1.1\r\n" +
                    "Host: httpbin.org\r\n" +
                    "Connection: keep-alive\r\n\r\n";
            out.write(request1.getBytes(StandardCharsets.UTF_8));
            out.flush();

            // Odczyt odpowiedzi na pierwsze żądanie
            System.out.println("Odpowiedź na pierwsze żądanie:");
            readResponse(in);

            // Drugie żądanie w tym samym połączeniu
            String request2 = "GET /ip HTTP/1.1\r\n" +
                    "Host: httpbin.org\r\n" +
                    "Connection: keep-alive\r\n\r\n";
            out.write(request2.getBytes(StandardCharsets.UTF_8));
            out.flush();

            // Odczyt odpowiedzi na drugie żądanie
            System.out.println("Odpowiedź na drugie żądanie:");
            readResponse(in);

            // Zamknięcie połączenia przez klienta
            String closeRequest = "GET /status/200 HTTP/1.1\r\n" +
                    "Host: httpbin.org\r\n" +
                    "Connection: close\r\n\r\n";
            out.write(closeRequest.getBytes(StandardCharsets.UTF_8));
            out.flush();

            // Odczyt odpowiedzi na zamykające żądanie
            System.out.println("Odpowiedź na ostatnie żądanie:");
            readResponse(in);
        }
    }

    private static void readResponse(InputStream in) throws Exception {
        byte[] buffer = new byte[1024];
        int bytesRead;
        while ((bytesRead = in.read(buffer)) != -1) {
            String response = new String(buffer, 0, bytesRead, StandardCharsets.UTF_8);
            System.out.print(response);
            // Koniec odpowiedzi HTTP (przykład uproszczony)
            if (response.contains("\r\n\r\n")) break;
        }
        System.out.println();
    }
}
