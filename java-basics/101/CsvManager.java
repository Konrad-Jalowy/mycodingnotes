import java.io.*;
import java.nio.file.*;
import java.util.*;

public class CsvManager {
    private static final String FILE_NAME = "people.csv";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean exit = false;

        while (!exit) {
            System.out.println("\n--- Zarządzanie danymi w CSV ---");
            System.out.println("1. Wyświetl osoby");
            System.out.println("2. Dodaj nową osobę");
            System.out.println("3. Usuń wszystkie osoby");
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
                case 1 -> displayPeople();
                case 2 -> addPerson(scanner);
                case 3 -> deleteAllPeople();
                case 4 -> {
                    System.out.println("Zamykanie programu. Do zobaczenia!");
                    exit = true;
                }
                default -> System.out.println("Nieprawidłowa opcja. Wybierz od 1 do 4.");
            }
        }

        scanner.close();
    }

    // 1. Wyświetlanie osób z CSV
    private static void displayPeople() {
        try {
            List<String> lines = Files.readAllLines(Paths.get(FILE_NAME));
            if (lines.isEmpty()) {
                System.out.println("Brak danych w pliku.");
                return;
            }

            System.out.println("\n--- Lista osób ---");
            for (String line : lines) {
                String[] data = line.split(",");
                System.out.printf("Imię: %s, Nazwisko: %s, Wiek: %s%n", data[0], data[1], data[2]);
            }
        } catch (NoSuchFileException e) {
            System.out.println("Plik CSV nie istnieje. Dodaj pierwszą osobę!");
        } catch (IOException e) {
            System.out.println("Wystąpił błąd podczas odczytu pliku: " + e.getMessage());
        }
    }

    // 2. Dodawanie osoby do CSV
    private static void addPerson(Scanner scanner) {
        System.out.print("Podaj imię: ");
        String firstName = scanner.nextLine();

        System.out.print("Podaj nazwisko: ");
        String lastName = scanner.nextLine();

        System.out.print("Podaj wiek: ");
        String age = scanner.nextLine();

        String person = firstName + "," + lastName + "," + age;

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME, true))) {
            writer.write(person);
            writer.newLine();
            System.out.println("Dodano osobę: " + person);
        } catch (IOException e) {
            System.out.println("Wystąpił błąd podczas zapisu do pliku: " + e.getMessage());
        }
    }

    // 3. Usuwanie wszystkich danych z CSV
    private static void deleteAllPeople() {
        try {
            Files.deleteIfExists(Paths.get(FILE_NAME));
            System.out.println("Wszystkie dane zostały usunięte.");
        } catch (IOException e) {
            System.out.println("Wystąpił błąd podczas usuwania pliku: " + e.getMessage());
        }
    }
}
