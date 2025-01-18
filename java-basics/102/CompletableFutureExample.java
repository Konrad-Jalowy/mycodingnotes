
import java.util.concurrent.CompletableFuture;

public class CompletableFutureExample {
    public static void main(String[] args) {
        System.out.println("Start programu...");

        // Zadanie 1: Symulacja pobierania danych z API
        CompletableFuture<String> apiData = CompletableFuture.supplyAsync(() -> {
            System.out.println("Pobieranie danych z API...");
            try {
                Thread.sleep(2000); // Symulacja czasu przetwarzania
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            return "Dane z API";
        });

        // Zadanie 2: Symulacja pobierania danych z bazy danych
        CompletableFuture<String> dbData = CompletableFuture.supplyAsync(() -> {
            System.out.println("Pobieranie danych z bazy danych...");
            try {
                Thread.sleep(3000); // Symulacja czasu przetwarzania
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            return "Dane z bazy danych";
        });

        // Zadanie 3: Symulacja odczytu danych z pliku
        CompletableFuture<String> fileData = CompletableFuture.supplyAsync(() -> {
            System.out.println("Odczyt danych z pliku...");
            try {
                Thread.sleep(1000); // Symulacja czasu przetwarzania
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            return "Dane z pliku";
        });

        // Scalenie wyników po zakończeniu wszystkich zadań
        CompletableFuture<Void> allTasks = CompletableFuture.allOf(apiData, dbData, fileData)
                .thenRun(() -> {
                    try {
                        // Odczyt wyników wszystkich zadań
                        String apiResult = apiData.get();
                        String dbResult = dbData.get();
                        String fileResult = fileData.get();

                        System.out.println("Wszystkie zadania zakończone.");
                        System.out.println("Wynik API: " + apiResult);
                        System.out.println("Wynik DB: " + dbResult);
                        System.out.println("Wynik Plik: " + fileResult);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                });

        System.out.println("Program nie czeka na zakończenie zadań.");
        allTasks.join(); // Czekamy na zakończenie wszystkich zadań
        System.out.println("Program zakończony.");
    }
}
