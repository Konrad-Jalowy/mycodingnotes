import java.io.File;
import java.io.IOException;

public class FileExample {
    public static void main(String[] args) throws IOException {
        File file = new File("example.txt");

        // Tworzenie nowego pliku
        if (file.createNewFile()) {
            System.out.println("Plik utworzony: " + file.getName());
        } else {
            System.out.println("Plik już istnieje.");
        }

        // Informacje o pliku
        System.out.println("Nazwa: " + file.getName());
        System.out.println("Ścieżka: " + file.getAbsolutePath());
        System.out.println("Rozmiar: " + file.length() + " bajtów");

        // Usuwanie pliku
        if (file.delete()) {
            System.out.println("Plik usunięty.");
        }
    }
}
