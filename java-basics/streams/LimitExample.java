import java.util.*;
import java.util.stream.Collectors; // Upewnij się, że to jest zaimportowane!

public class LimitExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve");

        List<String> limited = names.stream()
                .limit(3) // Pobierz tylko 3 pierwsze elementy
                .collect(Collectors.toList()); // Zbieranie wyników do listy

        System.out.println("Ograniczona lista: " + limited);
    }
}
