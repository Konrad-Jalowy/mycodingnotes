

import java.util.LinkedList;
public class offerandpoll {
    public static void main(String[] args) {
        LinkedList<String> queue = new LinkedList<>();

        // Dodawanie do kolejki
        queue.offer("Jan");
        queue.offer("Anna");
        queue.offer("Piotr");

        // Obsługa kolejki
        while (!queue.isEmpty()) {
            System.out.println("Obsługa: " + queue.poll());
        }
    }
}


