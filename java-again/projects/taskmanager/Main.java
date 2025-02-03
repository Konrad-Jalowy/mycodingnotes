public class Main {
    public static void main(String[] args) {
        TaskManager taskManager = new TaskManager();

        // Zadanie 1: Symulacja pobierania pliku
        taskManager.addTask(() -> {
            System.out.println("Pobieranie pliku...");
            try { Thread.sleep(3000); } catch (InterruptedException ignored) {}
            System.out.println("Plik pobrany!");
        });

        // Zadanie 2: Symulacja zapisu do bazy danych
        taskManager.addTask(() -> {
            System.out.println("Zapisywanie danych do bazy...");
            try { Thread.sleep(2000); } catch (InterruptedException ignored) {}
            System.out.println("Dane zapisane w bazie!");
        });

        // Zadanie 3: Symulacja wysyłania e-maila
        taskManager.addTask(() -> {
            System.out.println("Wysyłanie e-maila...");
            try { Thread.sleep(2500); } catch (InterruptedException ignored) {}
            System.out.println("E-mail wysłany!");
        });

        // Uruchomienie wszystkich zadań
        taskManager.startAll();

        // Czekamy na zakończenie wszystkich zadań
        taskManager.waitForCompletion();
    }
}
