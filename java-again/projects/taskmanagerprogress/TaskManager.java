import java.util.ArrayList;
import java.util.List;

class TaskManager {
    private final List<Thread> threads = new ArrayList<>();

    public void addTask(Runnable task) {
        Thread thread = new Thread(task);
        threads.add(thread);
    }

    public void startAll() {
        System.out.println("Uruchamiam wszystkie zadania...\n");
        for (Thread thread : threads) {
            thread.start();
        }
    }

    public void waitForCompletion() {
        for (Thread thread : threads) {
            try {
                thread.join(); // Czekamy na zakończenie każdego wątku
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("\n✅ Wszystkie zadania zakończone!");
    }
}
