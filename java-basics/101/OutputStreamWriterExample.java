import java.io.FileOutputStream;
import java.io.OutputStreamWriter;
import java.io.Writer;

public class OutputStreamWriterExample {
    public static void main(String[] args) {
        String data = "Przykład tekstu do zapisania.";
        try (Writer writer = new OutputStreamWriter(new FileOutputStream("output.txt"), "UTF-8")) {
            writer.write(data); // Zapis znaków
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
