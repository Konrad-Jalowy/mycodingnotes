import com.google.gson.Gson;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import java.io.IOException;

class Post {
    int id;
    String title;
    String body;
}

public class Gson8 {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient();
        String url = "https://jsonplaceholder.typicode.com/posts/1";

        // Użycie try-with-resources
        Request request = new Request.Builder().url(url).build();
        try (Response response = client.newCall(request).execute()) {
            if (response.isSuccessful() && response.body() != null) {
                    Gson gson = new Gson();
                    Post post = gson.fromJson(response.body().string(), Post.class);
                    System.out.println("Title: " + post.title);
                    System.out.println("Body: " + post.body);
            } else {
                System.out.println("Request failed: " + response.code());
            }
        } catch (IOException e) {
            System.err.println("Błąd podczas wykonywania żądania: " + e.getMessage());
        }
    }
}
