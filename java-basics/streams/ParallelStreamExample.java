
import java.util.*;

public class ParallelStreamExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        numbers.parallelStream() // Tworzenie równoległego strumienia
                .map(n -> n * n) // Podnieś do kwadratu
                .forEach(n -> System.out.println("Wynik: " + n + " w wątku: " + Thread.currentThread().getName()));
    }
}
