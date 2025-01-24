import java.util.Map;

public class NestedMapRecursion {
    public static void main(String[] args) {
        Map<String, Object> nestedMap = Map.of(
                "Alice", Map.of("Math", 90, "English", 85),
                "Bob", Map.of("Math", 80, "Science", 88)
        );

        processMap(nestedMap);
    }

    static void processMap(Map<String, Object> map) {
        for (Map.Entry<String, Object> entry : map.entrySet()) {
            System.out.println("Klucz: " + entry.getKey());
            if (entry.getValue() instanceof Map) {
                System.out.println("  Wartość jest zagnieżdżoną mapą:");
                processMap((Map<String, Object>) entry.getValue());
            } else {
                System.out.println("  Wartość: " + entry.getValue());
            }
        }
    }
}