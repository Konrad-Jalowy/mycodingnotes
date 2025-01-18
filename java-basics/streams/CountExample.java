import java.util.*;

public class CountExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);

        long evenCount = numbers.stream()
                .filter(n -> n % 2 == 0) // Filtrowanie liczb parzystych
                .count(); // Liczenie elementów

        System.out.println("Liczba parzystych: " + evenCount);
    }
}
