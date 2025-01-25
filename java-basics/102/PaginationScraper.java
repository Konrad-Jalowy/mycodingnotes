import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class PaginationScraper {
    public static void main(String[] args) {
        String baseUrl = "http://books.toscrape.com/catalogue/page-";
        int page = 1;

        try {
            while (true) {
                // Pobierz stronę z książkami
                String url = baseUrl + page + ".html";
                Document doc = Jsoup.connect(url).get();

                // Pobierz książki
                Elements books = doc.select(".product_pod");
                if (books.isEmpty()) break; // Jeśli nie ma więcej książek, zakończ

                // Iteracja przez książki na stronie
                for (Element book : books) {
                    String title = book.select("h3 a").attr("title");
                    String price = book.select(".price_color").text();
                    System.out.println("Tytuł: " + title + ", Cena: " + price);
                }

                page++; // Przejdź do następnej strony
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
