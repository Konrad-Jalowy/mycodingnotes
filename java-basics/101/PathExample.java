import java.nio.file.Path;
import java.nio.file.Paths;

public class PathExample {
    public static void main(String[] args) {
        Path path = Paths.get("example.txt");
        System.out.println("Nazwa pliku: " + path.getFileName());
        System.out.println("Katalog nadrzędny: " + path.getParent());
    }
}
