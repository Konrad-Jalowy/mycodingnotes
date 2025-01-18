import java.util.Arrays;

public class ArrayStreamExample {
    public static void main(String[] args) {
        String[] words = {"apple", "banana", "cherry", "date"};

        Arrays.stream(words)
                .filter(word -> word.length() > 5) // Filtrowanie słów dłuższych niż 5 znaków
                .map(String::toUpperCase) // Zamiana na wielkie litery
                .forEach(System.out::println); // Wypisz każde słowo
    }
}
