import java.util.*;
import java.util.stream.Collectors;

public class MapExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

        List<String> upperCaseNames = names.stream()
                .map(String::toUpperCase) // Transformacja na wielkie litery
                .collect(Collectors.toList());

        System.out.println("Wielkie litery: " + upperCaseNames);
    }
}
