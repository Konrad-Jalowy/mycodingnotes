import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class ProducerConsumerExample {
    public static void main(String[] args) {
        BlockingQueue<String> queue = new LinkedBlockingQueue<>();

        Thread producer = new Thread(() -> {
            try {
                queue.put("Dane 1");
                queue.put("Dane 2");
                System.out.println("Producent: dane w kolejce.");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        Thread consumer = new Thread(() -> {
            try {
                System.out.println("Konsument odebrał: " + queue.take());
                System.out.println("Konsument odebrał: " + queue.take());
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        producer.start();
        consumer.start();
    }
}
