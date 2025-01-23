import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

import java.io.IOException;

public class ApiFetcher {
    private static final String API_URL = "https://jsonplaceholder.typicode.com/posts";

    public static void main(String[] args) {
        ApiFetcher fetcher = new ApiFetcher();
        fetcher.fetchAndPrintPosts();
    }

    public void fetchAndPrintPosts() {
        OkHttpClient client = new OkHttpClient();

        Request request = new Request.Builder()
                .url(API_URL)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                System.err.println("Błąd w żądaniu: " + response.code());
                return;
            }

            String responseBody = response.body().string();

            // Parsowanie JSON za pomocą Gson
            Gson gson = new Gson();
            JsonArray posts = gson.fromJson(responseBody, JsonArray.class);

            // Iteracja po wynikach
            for (JsonElement post : posts) {
                System.out.println("Post ID: " + post.getAsJsonObject().get("id").getAsInt());
                System.out.println("Title: " + post.getAsJsonObject().get("title").getAsString());
                System.out.println("Body: " + post.getAsJsonObject().get("body").getAsString());
                System.out.println("----");
            }
        } catch (IOException e) {
            System.err.println("Błąd podczas pobierania danych: " + e.getMessage());
        }
    }
}