import com.rometools.rome.io.SyndFeedInput;
import com.rometools.rome.io.XmlReader;
import com.rometools.rome.feed.synd.SyndFeed;

import java.net.URL;

public class RSSReader {
    public static void main(String[] args) {
        try {
            URL feedUrl = new URL("https://www.polsatnews.pl/rss/wszystkie.xml");
            SyndFeedInput input = new SyndFeedInput();
            SyndFeed feed = input.build(new XmlReader(feedUrl));

            System.out.println("Tytuł kanału: " + feed.getTitle());
            feed.getEntries().forEach(entry -> {
                System.out.println("Tytuł artykułu: " + entry.getTitle());
                System.out.println("Link: " + entry.getLink());
            });
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}