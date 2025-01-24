import okhttp3.*;

import java.io.IOException;

public class MultipleRequestsExample {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient();

        String[] urls = {
                "https://jsonplaceholder.typicode.com/posts/1",
                "https://jsonplaceholder.typicode.com/posts/2",
                "https://jsonplaceholder.typicode.com/posts/3"
        };

        for (String url : urls) {
            Request request = new Request.Builder()
                    .url(url)
                    .build();

            client.newCall(request).enqueue(new Callback() {
                @Override
                public void onFailure(Call call, IOException e) {
                    System.err.println("Błąd podczas zapytania do " + url + ": " + e.getMessage());
                }

                @Override
                public void onResponse(Call call, Response response) throws IOException {
                    if (!response.isSuccessful()) {
                        System.err.println("Błąd serwera dla " + url + ": " + response.code());
                        return;
                    }

                    System.out.println("Odpowiedź z " + url + ":");
                    System.out.println(response.body().string());
                }
            });
        }

        System.out.println("Wysłano wszystkie zapytania...");
    }
}
