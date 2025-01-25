import java.nio.file.Files;
import java.nio.file.Path;

public class FileExistsExample {
    public static void main(String[] args) {
        Path path = Path.of("example.txt");

        if (Files.exists(path)) {
            System.out.println("Plik istnieje.");
        } else {
            System.out.println("Plik nie istnieje.");
        }
    }
}
