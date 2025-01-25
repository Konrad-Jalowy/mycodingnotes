import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import java.util.concurrent.CompletableFuture;

public class AsyncJsoupExample {
    public static void main(String[] args) {
        String url = "https://example.com";

        // Asynchroniczne pobieranie strony
        CompletableFuture<Void> future = CompletableFuture.runAsync(() -> {
            try {
                Document doc = Jsoup.connect(url).get();
                System.out.println("Tytuł strony: " + doc.title());
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
        System.out.println("To się wykonuje nie czekając");
        // Czekanie na zakończenie asynchronicznej operacji
        future.join();

        System.out.println("To jest wykonywane po zakończeniu pobierania strony.");
    }
}
