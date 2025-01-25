import java.net.URL;

public class URLExample {
    public static void main(String[] args) {
        try {
            // Tworzenie obiektu URL
            URL url = new URL("https://example.com:8080/page?name=John#section2");

            // Wyświetlanie elementów URL
            System.out.println("Protokół: " + url.getProtocol()); // https
            System.out.println("Host: " + url.getHost());         // example.com
            System.out.println("Port: " + url.getPort());         // 8080
            System.out.println("Ścieżka: " + url.getPath());      // /page
            System.out.println("Query: " + url.getQuery());       // name=John
            System.out.println("Fragment: " + url.getRef());      // section2
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
