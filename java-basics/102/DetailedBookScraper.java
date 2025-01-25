import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class DetailedBookScraper {
    public static void main(String[] args) {
        try {
            Document doc = Jsoup.connect("http://books.toscrape.com").get();

            // Pobierz linki do szczegółowych stron książek
            Elements bookLinks = doc.select(".product_pod h3 a");

            for (Element link : bookLinks) {
                String bookUrl = "http://books.toscrape.com/" + link.attr("href"); // Link do książki
                Document bookDoc = Jsoup.connect(bookUrl).get();

                // Pobierz szczegóły książki
                String title = bookDoc.select("h1").text();
                String description = bookDoc.select("#product_description + p").text();
                String availability = bookDoc.select(".availability").text();

                System.out.println("Tytuł: " + title);
                System.out.println("Opis: " + description);
                System.out.println("Dostępność: " + availability);
                System.out.println("---------------------------------");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

