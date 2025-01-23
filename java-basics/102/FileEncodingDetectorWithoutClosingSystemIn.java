import java.io.*;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Scanner;

public class FileEncodingDetectorWithoutClosingSystemIn {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Nie zamykamy System.in

        try {
            // Pobierz ścieżkę pulpitu
            String desktopPath = System.getProperty("user.home") + File.separator + "Desktop";

            // Zapytaj użytkownika o nazwę pliku
            System.out.print("Podaj nazwę pliku (bez lub z .txt): ");
            String fileName = scanner.nextLine().trim();

            // Dodaj rozszerzenie .txt, jeśli brak
            if (!fileName.endsWith(".txt")) {
                fileName += ".txt";
            }

            // Pełna ścieżka pliku
            String filePath = desktopPath + File.separator + fileName;

            // Sprawdź, czy plik istnieje
            File file = new File(filePath);
            if (!file.exists()) {
                System.out.println("Plik '" + filePath + "' nie istnieje na pulpicie.");
                return;
            }

            // Wczytaj zawartość pliku jako bajty
            byte[] fileBytes = Files.readAllBytes(Paths.get(filePath));

            // Wykryj kodowanie
            Charset detectedEncoding = detectEncoding(fileBytes);

            System.out.println("Wykryte kodowanie: " + detectedEncoding.name());

            // Jeśli UTF-8, sprawdź BOM
            if (detectedEncoding.equals(StandardCharsets.UTF_8)) {
                boolean hasBom = hasUtf8Bom(fileBytes);
                System.out.println("UTF-8 BOM: " + (hasBom ? "Tak" : "Nie"));
            }

        } catch (IOException e) {
            System.out.println("Wystąpił błąd: " + e.getMessage());
        } finally {
            // Scanner nie jest zamykany, aby System.in pozostał otwarty
            System.out.println("Program zakończony, ale System.in pozostaje otwarty.");
        }
    }

    // Metoda do wykrywania kodowania
    private static Charset detectEncoding(byte[] fileBytes) {
        // Sprawdź, czy plik ma BOM
        if (fileBytes.length >= 3 &&
                fileBytes[0] == (byte) 0xEF && fileBytes[1] == (byte) 0xBB && fileBytes[2] == (byte) 0xBF) {
            return StandardCharsets.UTF_8; // UTF-8 z BOM
        } else if (fileBytes.length >= 2 &&
                fileBytes[0] == (byte) 0xFF && fileBytes[1] == (byte) 0xFE) {
            return StandardCharsets.UTF_16LE; // UTF-16 LE z BOM
        } else if (fileBytes.length >= 2 &&
                fileBytes[0] == (byte) 0xFE && fileBytes[1] == (byte) 0xFF) {
            return StandardCharsets.UTF_16BE; // UTF-16 BE z BOM
        }

        // Domyślne kodowanie (zakładamy systemowe)
        return Charset.defaultCharset();
    }

    // Metoda do sprawdzania obecności BOM w UTF-8
    private static boolean hasUtf8Bom(byte[] fileBytes) {
        return fileBytes.length >= 3 &&
                fileBytes[0] == (byte) 0xEF && fileBytes[1] == (byte) 0xBB && fileBytes[2] == (byte) 0xBF;
    }
}
