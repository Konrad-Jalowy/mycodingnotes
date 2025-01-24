import okhttp3.*;

import java.io.IOException;

public class AsyncHttpExample {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient();

        Request request = new Request.Builder()
                .url("https://jsonplaceholder.typicode.com/posts/1")
                .build();

        System.out.println("Wysyłanie zapytania asynchronicznego...");

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

                String responseData = response.body().string();
                System.out.println("Otrzymano odpowiedź:");
                System.out.println(responseData);
            }
        });

        System.out.println("Główny wątek kontynuuje pracę...");
    }
}
