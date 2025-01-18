import java.util.*;
import java.util.stream.Collectors;

public class JoiningExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

        String result = names.stream()
                .collect(Collectors.joining(", ")); // Łączenie ciągów znaków

        System.out.println("Połączone imiona: " + result);
    }
}