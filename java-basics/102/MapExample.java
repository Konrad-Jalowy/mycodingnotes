import java.util.HashMap;
import java.util.Map;

public class MapExample {
    public static void main(String[] args) {
        // Tworzenie HashMap
        Map<String, Integer> ageMap = new HashMap<>();

        // Dodawanie elementów
        ageMap.put("Alice", 25);
        ageMap.put("Bob", 30);
        ageMap.put("Charlie", 35);

        // Wyświetlanie mapy
        System.out.println("Mapa: " + ageMap);

        // Pobieranie wartości
        System.out.println("Wiek Alice: " + ageMap.get("Alice"));

        // Iteracja po mapie
        System.out.println("Iteracja po mapie:");
        for (Map.Entry<String, Integer> entry : ageMap.entrySet()) {
            System.out.println("Klucz: " + entry.getKey() + ", Wartość: " + entry.getValue());
        }

        // Sprawdzanie obecności klucza/wartości
        System.out.println("Czy mapa zawiera klucz 'Bob'? " + ageMap.containsKey("Bob"));
        System.out.println("Czy mapa zawiera wartość 30? " + ageMap.containsValue(30));

        // Usuwanie elementów
        ageMap.remove("Charlie");
        System.out.println("Mapa po usunięciu 'Charlie': " + ageMap);

        // Rozmiar mapy
        System.out.println("Rozmiar mapy: " + ageMap.size());
    }
}