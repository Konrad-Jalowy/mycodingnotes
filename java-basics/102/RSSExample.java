import com.rometools.rome.feed.synd.SyndFeed;
import com.rometools.rome.feed.synd.SyndEntry;
import com.rometools.rome.io.SyndFeedInput;
import com.rometools.rome.io.XmlReader;

import java.net.URL;
import java.util.List;

public class RSSExample {
    public static void main(String[] args) {
        try {
            // URL kanału RSS
            URL feedUrl = new URL("https://www.polsatnews.pl/rss/wszystkie.xml");

            // Wczytanie kanału RSS
            SyndFeedInput input = new SyndFeedInput();
            SyndFeed feed = input.build(new XmlReader(feedUrl));

            // Pobranie wpisów z kanału RSS
            List<SyndEntry> entries = feed.getEntries();

            // Iteracja po wpisach i wyświetlenie ich szczegółów
            for (SyndEntry entry : entries) {
                System.out.println("Tytuł: " + entry.getTitle());
                System.out.println("Link: " + entry.getLink());
                System.out.println("Data publikacji: " + entry.getPublishedDate());
                System.out.println("Opis: " + (entry.getDescription() != null ? entry.getDescription().getValue() : "Brak opisu"));
                System.out.println("----------------------------------------");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
