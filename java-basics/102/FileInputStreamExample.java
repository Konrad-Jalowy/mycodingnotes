import java.io.FileInputStream;
import java.io.InputStream;

public class FileInputStreamExample {
    public static void main(String[] args) {
        try (InputStream inputStream = new FileInputStream("example.txt")) {
            int data;
            while ((data = inputStream.read()) != -1) { // Odczyt bajt po bajcie
                System.out.print((char) data); // Konwersja bajtu na znak
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
