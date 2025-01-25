import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class ReadFileExample {
    public static void main(String[] args) throws Exception {
        Path path = Path.of("example.txt");

        // Odczyt wszystkich linii
        List<String> lines = Files.readAllLines(path);
        lines.forEach(System.out::println);
    }
}
