class SharedResource {
    private boolean isAvailable = false;

    public synchronized void produce() {
        isAvailable = true;
        System.out.println("Producent: dane gotowe.");
        notify(); // Powiadomienie konsumenta
    }

    public synchronized void consume() {
        while (!isAvailable) {
            try {
                wait(); // Konsument czeka na dane
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("Konsument: dane odebrane.");
    }
}

public class WaitNotifyExample {
    public static void main(String[] args) {
        SharedResource resource = new SharedResource();

        Thread producer = new Thread(resource::produce);
        Thread consumer = new Thread(resource::consume);

        consumer.start();
        producer.start();
    }
}
