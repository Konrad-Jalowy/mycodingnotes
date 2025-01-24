import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.Scanner;

public class TerminalBrowser {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Terminal Browser ===");
        System.out.print("Wprowadź URL (np. https://example.com): ");
        String url = scanner.nextLine();

        try {
            // Pobranie strony za pomocą Jsoup
            Document doc = Jsoup.connect(url).get();

            // Wyświetlenie tytułu strony
            System.out.println("\n=== Tytuł strony ===");
            System.out.println(doc.title());

            // Wyświetlenie nagłówków
            System.out.println("\n=== Nagłówki ===");
            Elements headers = doc.select("h1, h2, h3, h4, h5, h6");
            for (Element header : headers) {
                System.out.println(header.tagName().toUpperCase() + ": " + header.text());
            }

            // Wyświetlenie linków
            System.out.println("\n=== Linki ===");
            Elements links = doc.select("a[href]");
            for (Element link : links) {
                System.out.println(link.text() + " -> " + link.attr("href"));
            }

            // Wyświetlenie paragrafów
            System.out.println("\n=== Zawartość strony ===");
            Elements paragraphs = doc.select("p");
            for (Element paragraph : paragraphs) {
                System.out.println(paragraph.text());
                System.out.println("----");
            }

        } catch (IOException e) {
            System.err.println("Błąd podczas pobierania strony: " + e.getMessage());
        }
    }
}
