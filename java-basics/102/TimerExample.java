import java.util.Timer;
import java.util.TimerTask;

public class TimerExample {
    public static void main(String[] args) {
        Timer timer = new Timer();

        // Tworzymy zadanie TimerTask
        TimerTask task = new TimerTask() {
            int counter = 0;

            @Override
            public void run() {
                counter++;
                System.out.println("Counter: " + counter);
                if (counter == 5) {
                    System.out.println("Stopping timer.");
                    timer.cancel(); // Anulowanie działania timera
                }
            }
        };

        // Zaplanowanie zadania do wykonywania co sekundę
        timer.scheduleAtFixedRate(task, 0, 1000);

        System.out.println("Timer started...");
    }
}
