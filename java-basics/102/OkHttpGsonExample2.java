import com.google.gson.Gson;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class OkHttpGsonExample2 {
    public static void main(String[] args) {
        // Klient HTTP
        OkHttpClient client = new OkHttpClient();

        // Żądanie GET
        Request request = new Request.Builder()
                .url("https://jsonplaceholder.typicode.com/users/1")
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (response.isSuccessful() && response.body() != null) {
                // Pobranie treści odpowiedzi jako JSON
                String json = response.body().string();

                // Parsowanie JSON do obiektu Java
                Gson gson = new Gson();
                User user = gson.fromJson(json, User.class);

                System.out.println("ID: " + user.getId());
                System.out.println("Name: " + user.getName());
                System.out.println("Email: " + user.getEmail());
            } else {
                System.err.println("Błąd: " + response.code());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// Klasa reprezentująca dane użytkownika
class User {
    private int id;
    private String name;
    private String email;

    public int getId() { return id; }
    public String getName() { return name; }
    public String getEmail() { return email; }
}
