import java.util.*;
import java.util.stream.Collectors;

public class GroupingExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Anna", "Charlie", "Alex");

        Map<Character, List<String>> groupedByFirstLetter = names.stream()
                .collect(Collectors.groupingBy(name -> name.charAt(0))); // Grupowanie po pierwszej literze

        System.out.println(groupedByFirstLetter);
    }
}
