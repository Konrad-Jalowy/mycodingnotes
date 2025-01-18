
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.locks.ReentrantLock;

public class OrderProcessingSystem {
    private static final int MAX_THREADS = 5; // Maksymalna liczba jednoczesnych wątków
    private static int totalOrdersProcessed = 0; // Licznik przetworzonych zamówień
    private static final ReentrantLock lock = new ReentrantLock(); // Synchronizacja dla licznika

    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(MAX_THREADS);

        System.out.println("System przetwarzania zamówień uruchomiony...");

        for (int i = 1; i <= 20; i++) {
            int orderId = i; // Każde zamówienie ma unikalny ID
            executor.submit(() -> processOrder(orderId));
        }

        executor.shutdown(); // Nie przyjmujemy nowych zadań, czekamy na zakończenie istniejących
        while (!executor.isTerminated()) {
            // Czekamy, aż wszystkie wątki zakończą działanie
        }

        System.out.println("Wszystkie zamówienia zostały przetworzone.");
        System.out.println("Łączna liczba przetworzonych zamówień: " + totalOrdersProcessed);
    }

    private static void processOrder(int orderId) {
        System.out.println("Przetwarzanie zamówienia: " + orderId);

        // Symulacja czasu przetwarzania zamówienia (np. obsługa płatności, pakowanie)
        try {
            Thread.sleep((long) (Math.random() * 2000) + 1000); // 1-3 sekundy
        } catch (InterruptedException e) {
            System.out.println("Zamówienie " + orderId + " zostało przerwane.");
        }

        // Synchronizowany dostęp do licznika zamówień
        lock.lock();
        try {
            totalOrdersProcessed++;
            System.out.println("Zamówienie " + orderId + " zostało zakończone. Łącznie przetworzono: " + totalOrdersProcessed);
        } finally {
            lock.unlock();
        }
    }
}
