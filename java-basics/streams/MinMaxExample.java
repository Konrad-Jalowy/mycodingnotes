import java.util.*;

public class MinMaxExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(42, 15, 23, 8, 34);

        int min = numbers.stream()
                .min(Integer::compareTo) // Znajdź najmniejszą wartość
                .orElseThrow(); // Zwróć wyjątek, jeśli lista jest pusta

        int max = numbers.stream()
                .max(Integer::compareTo) // Znajdź największą wartość
                .orElseThrow();

        System.out.println("Min: " + min + ", Max: " + max);
    }
}
