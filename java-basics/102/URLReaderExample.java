import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

public class URLReaderExample {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://example.com");

            // Otwieranie strumienia wejściowego
            BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));

            // Czytanie zawartości strony
            String inputLine;
            while ((inputLine = in.readLine()) != null) {
                System.out.println(inputLine);
            }

            // Zamknięcie strumienia
            in.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}