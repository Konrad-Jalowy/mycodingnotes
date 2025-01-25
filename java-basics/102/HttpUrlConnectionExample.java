import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class HttpUrlConnectionExample {
    public static void main(String[] args) {
        try {
            // Tworzenie obiektu URL
            URL url = new URL("https://example.com");

            // Otwarcie połączenia
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            // Konfiguracja połączenia
            connection.setRequestMethod("GET"); // Typ żądania (GET)
            connection.setConnectTimeout(5000); // Czas oczekiwania na połączenie (ms)
            connection.setReadTimeout(5000);    // Czas oczekiwania na odpowiedź (ms)

            // Pobranie kodu statusu HTTP
            int status = connection.getResponseCode();
            System.out.println("Kod odpowiedzi: " + status);

            // Czytanie odpowiedzi, jeśli status jest OK (200)
            if (status == HttpURLConnection.HTTP_OK) {
                BufferedReader reader = new BufferedReader(
                        new InputStreamReader(connection.getInputStream()));
                StringBuilder response = new StringBuilder();
                String line;

                while ((line = reader.readLine()) != null) {
                    response.append(line);
                }
                reader.close();

                System.out.println("Treść odpowiedzi: " + response);
            }

            // Zamknięcie połączenia
            connection.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
