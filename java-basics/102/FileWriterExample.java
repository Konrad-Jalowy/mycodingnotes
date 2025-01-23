import java.io.FileWriter;
import java.io.IOException;

public class FileWriterExample {
    public static void main(String[] args) {
        try (FileWriter writer = new FileWriter("example.txt")) {
            writer.write("To jest zapis bez buforowania.\n");
            writer.write("Każde wywołanie write() działa bezpośrednio na pliku.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
