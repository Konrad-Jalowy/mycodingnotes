import okhttp3.*;

import java.io.IOException;

public class AsyncPostExample {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient();

        // Dane JSON do wysłania
        String json = "{\"title\":\"foo\",\"body\":\"bar\",\"userId\":1}";
        RequestBody body = RequestBody.create(json, MediaType.get("application/json; charset=utf-8"));

        Request request = new Request.Builder()
                .url("https://jsonplaceholder.typicode.com/posts")
                .post(body)
                .build();

        System.out.println("Wysyłanie zapytania POST...");

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
                System.out.println("Odpowiedź serwera:");
                System.out.println(responseData);
            }
        });

        System.out.println("Główny wątek kontynuuje pracę...");
    }
}
