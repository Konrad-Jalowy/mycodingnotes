import com.google.gson.*;
import okhttp3.*;

import java.io.IOException;
import java.util.List;

public class OkHttpGsonExample {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient();

        // Tworzenie żądania
        Request request = new Request.Builder()
                .url("https://jsonplaceholder.typicode.com/posts")
                .build();

        // Wysłanie zapytania asynchronicznie
        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                System.err.println("Błąd podczas zapytania: " + e.getMessage());
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (!response.isSuccessful()) {
                    System.err.println("Błąd serwera: " + response.code());
                    return;
                }

                // Parsowanie JSON za pomocą Gson
                String responseBody = response.body().string();
                Gson gson = new Gson();

                // Deserializacja JSON do listy obiektów Post
                List<Post> posts = List.of(gson.fromJson(responseBody, Post[].class));

                // Wyświetlenie wyników
                for (Post post : posts) {
                    System.out.println("Post ID: " + post.id);
                    System.out.println("Title: " + post.title);
                    System.out.println("Body: " + post.body);
                    System.out.println("----");
                }
            }
        });

        System.out.println("Zapytanie zostało wysłane...");
    }

    // Klasa reprezentująca dane JSON
    static class Post {
        int userId;
        int id;
        String title;
        String body;
    }
}