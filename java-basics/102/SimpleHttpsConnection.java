import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import javax.net.ssl.SSLSocket;
import javax.net.ssl.SSLSocketFactory;

public class SimpleHttpsConnection {
    public static void main(String[] args) throws Exception {
        String host = "www.onet.pl"; // Witryna z HTTPS
        int port = 443; // Domyślny port dla HTTPS

        System.out.println("Connecting to: " + host);

        // Tworzymy SSLSocket dla połączenia HTTPS
        try (SSLSocket socket = (SSLSocket) SSLSocketFactory.getDefault().createSocket(host, port)) {
            OutputStream output = socket.getOutputStream();
            BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            // Wysyłamy zapytanie HTTP/1.1
            String request = "GET / HTTP/1.1\r\n" +
                    "Host: " + host + "\r\n" +
                    "Connection: close\r\n\r\n";
            output.write(request.getBytes());
            output.flush();

            // Odczytujemy odpowiedź
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = input.readLine()) != null) {
                response.append(line).append("\n");
            }

            // Wyświetlamy pełną odpowiedź
            System.out.println("Response:\n" + response.toString());
        }
    }
}
