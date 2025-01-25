import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class BookScraper {
    public static void main(String[] args) {
        try {
            Document doc = Jsoup.connect("http://books.toscrape.com").get();

            // Wybierz wszystkie książki na stronie
            Elements books = doc.select(".product_pod");

            // Iteracja przez książki
            for (Element book : books) {
                String title = book.select("h3 a").attr("title"); // Tytuł książki
                String price = book.select(".price_color").text(); // Cena książki
                System.out.println("Tytuł: " + title + ", Cena: " + price);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}