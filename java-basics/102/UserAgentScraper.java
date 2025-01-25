import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class UserAgentScraper {
    public static void main(String[] args) {
        try {
            Document doc = Jsoup.connect("http://books.toscrape.com")
                    .header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
                    .get();

            System.out.println("Tytuł strony: " + doc.title());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
