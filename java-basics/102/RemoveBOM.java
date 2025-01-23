import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.charset.StandardCharsets;

public class RemoveBOM {
    public static void main(String[] args) throws Exception {
        byte[] bytes = Files.readAllBytes(Path.of("plik.txt"));

        // Sprawdź, czy plik zaczyna się od BOM
        if (bytes[0] == (byte) 0xEF && bytes[1] == (byte) 0xBB && bytes[2] == (byte) 0xBF) {
            // Usuń pierwsze 3 bajty (BOM)
            bytes = java.util.Arrays.copyOfRange(bytes, 3, bytes.length);
        }

        String content = new String(bytes, StandardCharsets.UTF_8);
        System.out.println(content);
    }
}