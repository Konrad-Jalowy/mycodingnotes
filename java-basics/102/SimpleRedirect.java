import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.Socket;

public class SimpleRedirect {
    public static void main(String[] args) throws Exception {
        String currentUrl = "http://google.com"; // Startujemy od HTTP
        boolean isRedirecting = true; // Flaga dla jednej obsługi przekierowania

        while (true) {
            // Parsujemy URL na protokół, host, port i ścieżkę
            String protocol = currentUrl.startsWith("https://") ? "https" : "http";
            String host = currentUrl.replace("https://", "").replace("http://", "").split("/")[0];
            String path = currentUrl.contains("/") && currentUrl.indexOf("/") > protocol.length() + 3
                    ? currentUrl.substring(currentUrl.indexOf("/", protocol.length() + 3))
                    : "/";
            int port = protocol.equals("https") ? 443 : 80;

            System.out.println("Connecting to: " + currentUrl);

            // Obsługa HTTPS za pomocą SSLSocket
            Socket socket;
            if (protocol.equals("https")) {
                socket = javax.net.ssl.SSLSocketFactory.getDefault().createSocket(host, port);
            } else {
                socket = new Socket(host, port);
            }

            try (socket) {
                OutputStream output = socket.getOutputStream();
                BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));

                // Wysyłamy zapytanie HTTP
                String request = "GET " + path + " HTTP/1.1\r\n" +
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

                // Parsujemy nagłówki
                String[] headers = response.toString().split("\r\n\r\n", 2);
                String header = headers[0];
                String body = headers.length > 1 ? headers[1] : "";

                System.out.println("Response Header:\n" + header);

                // Obsługujemy kod 200
                if (header.startsWith("HTTP/1.1 200")) {
                    System.out.println("Content:\n" + body);
                    break; // Sukces - kończymy
                }

                // Obsługujemy przekierowanie 301/302 (tylko raz)
                if (isRedirecting && (header.startsWith("HTTP/1.1 301") || header.startsWith("HTTP/1.1 302"))) {
                    String location = null;

                    // Nowa, uproszczona metoda wyciągania 'Location'
                    if (header.toLowerCase().contains("location:")) {
                        int index = header.toLowerCase().indexOf("location:") + 9; // Przesuń za 'location:'
                        location = header.substring(index, header.indexOf("\n", index)).trim(); // Do końca linii
                        System.out.println("Found Location: " + location);
                    }

                    if (location == null || location.isEmpty()) {
                        System.out.println("Redirect without location! Exiting...");
                        break;
                    }

                    System.out.println("Redirected to: " + location);
                    currentUrl = location; // Przechodzimy na nowy adres
                    isRedirecting = false; // Tylko jedno przekierowanie
                } else {
                    System.out.println("Unhandled response or too many redirects.");
                    break;
                }
            }
        }
    }
}
