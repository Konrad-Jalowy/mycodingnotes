import java.nio.charset.Charset;

public class DefaultEncoding {
    public static void main(String[] args) {
        // Pobieranie domyślnego systemu kodowania
        Charset defaultCharset = Charset.defaultCharset();

        // Wyświetlenie domyślnego kodowania
        System.out.println("Domyślny system kodowania plików: " + defaultCharset.displayName());

        // Opcjonalnie: Wyświetlenie dodatkowych szczegółów
        System.out.println("Czy domyślne kodowanie obsługuje Unicode? " + defaultCharset.contains(Charset.forName("UTF-8")));
    }
}
