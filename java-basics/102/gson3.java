import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.lang.reflect.Type;
import java.util.List;

public class gson3 {
    public static void main(String[] args) {
        String json = "[{\"name\": \"Alice\", \"age\": 25}, {\"name\": \"Bob\", \"age\": 30}]";

        Gson gson = new Gson();

        // Definiujemy typ generyczny
        Type listType = new TypeToken<List<User>>() {}.getType();

        // Konwersja JSON → Lista obiektów
        List<User> users = gson.fromJson(json, listType);

        for (User user : users) {
            System.out.println("Name: " + user.name + ", Age: " + user.age);
        }
    }

    static class User {
        String name;
        int age;
    }
}
