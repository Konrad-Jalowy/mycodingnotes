import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class JsoupExample {
    public static void main(String[] args) {
        try {
            // Pobranie zawartości strony
            String url = "https://example.com";
            Document doc = Jsoup.connect(url).get();

            // Wyświetlenie tytułu strony
            System.out.println("Tytuł strony: " + doc.title());

            // Pobieranie linków
            Elements links = doc.select("a[href]");
            for (Element link : links) {
                System.out.println("Link: " + link.attr("href") + " Tekst: " + link.text());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
