import okhttp3.*;

import java.io.IOException;

public class OkHttpAsyncExample {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient();

        // Tworzenie żądania GET
        Request request = new Request.Builder()
                .url("https://jsonplaceholder.typicode.com/posts/1")
                .build();

        System.out.println("Wysyłanie zapytania asynchronicznego...");

        // Wysłanie zapytania asynchronicznie
        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                System.out.println("Błąd podczas zapytania: " + e.getMessage());
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (!response.isSuccessful()) {
                    System.out.println("Błąd serwera: " + response.code());
                    return;
                }

                // Pobranie i wypisanie odpowiedzi
                String responseData = response.body().string();
                System.out.println("Otrzymano odpowiedź:");
                System.out.println(responseData);
            }
        });

        // Informacja o zakończeniu programu
        System.out.println("Główny wątek kontynuuje pracę...");
    }
}
