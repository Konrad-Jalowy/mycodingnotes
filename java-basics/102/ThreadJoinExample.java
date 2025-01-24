public class ThreadJoinExample {
    public static void main(String[] args) {
        Runnable task = () -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("Thread is running: " + i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        };

        Thread thread = new Thread(task);
        thread.start(); // Uruchomienie wątku
        System.out.println("Main thread is running...");
        try {
            thread.join(); // Wątek główny czeka na zakończenie wątku "thread"
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Main thread is done.");
    }
}
