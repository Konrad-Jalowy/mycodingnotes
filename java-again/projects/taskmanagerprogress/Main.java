public class Main {
    public static void main(String[] args) {
        TaskManager taskManager = new TaskManager();

        // Dodajemy zadania z różnym czasem trwania
        taskManager.addTask(new ProgressTask("📂 Pobieranie pliku", 5000));  // 5 sekund
        taskManager.addTask(new ProgressTask("💾 Zapisywanie do bazy", 3000));  // 3 sekundy
        taskManager.addTask(new ProgressTask("📧 Wysyłanie e-maila", 4000));  // 4 sekundy

        // Uruchamiamy wszystkie zadania
        taskManager.startAll();

        // Czekamy na zakończenie
        taskManager.waitForCompletion();
    }
}
