import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.Reader;

public class InputStreamReaderExample {
    public static void main(String[] args) {
        try (Reader reader = new InputStreamReader(new FileInputStream("example.txt"), "UTF-8")) {
            int data;
            while ((data = reader.read()) != -1) { // Odczyt znak po znaku
                System.out.print((char) data);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
