package org.example;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> users = new ArrayList<>();

        while (true) {
            System.out.println("\n--- Menu ---");
            System.out.println("1. Dodaj użytkownika");
            System.out.println("2. Wyświetl użytkowników");
            System.out.println("3. Usuń użytkownika");
            System.out.println("4. Wyjście");
            System.out.print("Wybierz opcję: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Konsumuje znak nowej linii

            switch (choice) {
                case 1:
                    System.out.print("Podaj nazwę użytkownika: ");
                    String user = scanner.nextLine();
                    users.add(user);
                    System.out.println("Użytkownik dodany.");
                    break;
                case 2:
                    System.out.println("\nLista użytkowników:");
                    for (int i = 0; i < users.size(); i++) {
                        System.out.println((i + 1) + ". " + users.get(i));
                    }
                    break;
                case 3:
                    System.out.print("Podaj numer użytkownika do usunięcia: ");
                    int userIndex = scanner.nextInt();
                    scanner.nextLine(); // Konsumuje znak nowej linii
                    if (userIndex > 0 && userIndex <= users.size()) {
                        users.remove(userIndex - 1);
                        System.out.println("Użytkownik usunięty.");
                    } else {
                        System.out.println("Nieprawidłowy numer.");
                    }
                    break;
                case 4:
                    System.out.println("Koniec programu. Do widzenia!");
                    return;
                default:
                    System.out.println("Nieprawidłowa opcja. Spróbuj ponownie.");
            }
        }
    }
}
