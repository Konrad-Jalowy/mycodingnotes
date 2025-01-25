import java.io.FileOutputStream;
import java.io.OutputStream;

public class FileOutputStreamExample {
    public static void main(String[] args) {
        String data = "Przykładowy tekst do zapisania!";
        try (OutputStream outputStream = new FileOutputStream("output.txt")) {
            outputStream.write(data.getBytes()); // Konwersja String do tablicy bajtów
            System.out.println("Dane zapisane do pliku.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
