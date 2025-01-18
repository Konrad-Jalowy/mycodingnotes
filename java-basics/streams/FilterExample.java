
import java.util.*;
import java.util.stream.Collectors;

public class FilterExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Anna", "Charlie", "Alex");

        List<String> filteredNames = names.stream()
                .filter(name -> name.startsWith("A")) // Filtrowanie
                .collect(Collectors.toList()); // Zbieranie wyników do listy

        System.out.println("Imiona zaczynające się na 'A': " + filteredNames);
    }
}
