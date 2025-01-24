import okhttp3.*;

import java.io.IOException;

public class RequestWithHeadersExample {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient();

        HttpUrl url = new HttpUrl.Builder()
                .scheme("https")
                .host("jsonplaceholder.typicode.com")
                .addPathSegment("posts")
                .addQueryParameter("userId", "1") // Parametr w URL
                .build();

        Request request = new Request.Builder()
                .url(url)
                .header("User-Agent", "OkHttp Example") // Nagłówek User-Agent
                .header("Accept", "application/json") // Nagłówek Accept
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

                System.out.println("Otrzymano odpowiedź:");
                System.out.println(response.body().string());
            }
        });

        System.out.println("Wysłano zapytanie z nagłówkami...");
    }
}
