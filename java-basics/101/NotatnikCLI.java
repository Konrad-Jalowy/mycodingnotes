
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class NotatnikCLI {
    private static final String FILE_NAME = "notatki.txt";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean exit = false;

        while (!exit) {
            System.out.println("\n--- Notatnik CLI ---");
            System.out.println("1. Wyświetl notatki");
            System.out.println("2. Dodaj nową notatkę");
            System.out.println("3. Usuń wszystkie notatki");
            System.out.println("4. Wyjście");
            System.out.print("Wybierz opcję: ");

            int choice;
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Nieprawidłowy wybór. Spróbuj ponownie.");
                continue;
            }

            switch (choice) {
                case 1 -> displayNotes();
                case 2 -> addNote(scanner);
                case 3 -> deleteAllNotes();
                case 4 -> {
                    System.out.println("Zamykanie Notatnika. Do zobaczenia!");
                    exit = true;
                }
                default -> System.out.println("Nieprawidłowa opcja. Wybierz od 1 do 4.");
            }
        }

        scanner.close();
    }

    // 1. Wyświetlanie notatek
    private static void displayNotes() {
        try {
            List<String> notes = Files.readAllLines(Paths.get(FILE_NAME));
            if (notes.isEmpty()) {
                System.out.println("Brak notatek.");
            } else {
                System.out.println("\n--- Twoje notatki ---");
                for (int i = 0; i < notes.size(); i++) {
                    System.out.println((i + 1) + ". " + notes.get(i));
                }
            }
        } catch (NoSuchFileException e) {
            System.out.println("Brak pliku notatek. Dodaj pierwszą notatkę!");
        } catch (IOException e) {
            System.out.println("Wystąpił błąd podczas odczytu notatek: " + e.getMessage());
        }
    }

    // 2. Dodawanie nowej notatki
    private static void addNote(Scanner scanner) {
        System.out.print("Wpisz treść notatki: ");
        String note = scanner.nextLine();

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME, true))) {
            writer.write(note);
            writer.newLine();
            System.out.println("Dodano notatkę: " + note);
        } catch (IOException e) {
            System.out.println("Wystąpił błąd podczas zapisu notatki: " + e.getMessage());
        }
    }

    // 3. Usuwanie wszystkich notatek
    private static void deleteAllNotes() {
        try {
            Files.deleteIfExists(Paths.get(FILE_NAME));
            System.out.println("Wszystkie notatki zostały usunięte.");
        } catch (IOException e) {
            System.out.println("Wystąpił błąd podczas usuwania notatek: " + e.getMessage());
        }
    }
}
