import java.nio.file.Files;
import java.nio.file.Path;

public class HexReader {
    public static void main(String[] args) throws Exception {
        byte[] bytes = Files.readAllBytes(Path.of("plik.txt"));
        for (byte b : bytes) {
            System.out.printf("%02X ", b); // Wyświetla bajt w formacie hex
        }
    }
}
