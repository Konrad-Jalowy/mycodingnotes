import okhttp3.*;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

public class TimeoutExample {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(5, TimeUnit.SECONDS) // Timeout na połączenie
                .readTimeout(10, TimeUnit.SECONDS)   // Timeout na odczyt
                .build();

        Request request = new Request.Builder()
                .url("https://jsonplaceholder.typicode.com/posts/1")
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

        System.out.println("Wysłano zapytanie z timeoutem...");
    }
}
