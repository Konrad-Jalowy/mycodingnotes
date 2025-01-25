import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class WriteFileExample {
    public static void main(String[] args) throws Exception {
        Path path = Path.of("output.txt");

        // Zapis tekstu do pliku
        List<String> lines = List.of("Linia 1", "Linia 2", "Linia 3");
        Files.write(path, lines);

        System.out.println("Dane zapisane do pliku.");
    }
}
