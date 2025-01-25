import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class BufferedReaderExample {
    public static void main(String[] args) {
        try (BufferedReader bufferedReader = new BufferedReader(
                new InputStreamReader(new FileInputStream("example.txt"), "UTF-8"))) {

            String line;
            while ((line = bufferedReader.readLine()) != null) { // Odczyt linii tekstu
                System.out.println(line);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
