import com.rometools.rome.feed.synd.*;
import com.rometools.rome.io.SyndFeedInput;
import com.rometools.rome.io.XmlReader;

import java.net.URL;

public class RSSWithEnclosure {
    public static void main(String[] args) {
        try {
            // URL kanału RSS
            URL feedUrl = new URL("https://www.polsatnews.pl/rss/wszystkie.xml");
            SyndFeedInput input = new SyndFeedInput();
            SyndFeed feed = input.build(new XmlReader(feedUrl));

            // Iteracja po wpisach
            for (SyndEntry entry : feed.getEntries()) {
                System.out.println("Tytuł: " + entry.getTitle());

                // Pobranie elementów <enclosure>
                for (SyndEnclosure enclosure : entry.getEnclosures()) {
                    System.out.println("Enclosure URL: " + enclosure.getUrl());
                    System.out.println("Enclosure Type: " + enclosure.getType());
                    System.out.println("Enclosure Length: " + enclosure.getLength());
                }

                System.out.println("-------------------------------");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
