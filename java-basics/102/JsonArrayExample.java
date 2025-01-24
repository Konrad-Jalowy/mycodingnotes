import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import okhttp3.*;

import java.io.IOException;
import java.lang.reflect.Type;
import java.util.List;

public class JsonArrayExample {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient();

        Request request = new Request.Builder()
                .url("https://jsonplaceholder.typicode.com/posts") // Przykład API
                .build();

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

                String responseBody = response.body().string();
                Gson gson = new Gson();

                // Parsowanie tablicy JSON
                Type listType = new TypeToken<List<Post>>() {}.getType();
                List<Post> posts = gson.fromJson(responseBody, listType);

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

    static class Post {
        int userId;
        int id;
        String title;
        String body;
    }
}
