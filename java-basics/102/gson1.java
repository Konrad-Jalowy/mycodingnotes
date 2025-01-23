import com.google.gson.Gson;

class User {
    String name;
    int age;
}

public class gson1 {
    public static void main(String[] args) {
        String json = "{\"name\": \"Alice\", \"age\": 25}";

        // Tworzymy obiekt Gson
        Gson gson = new Gson();

        // Konwersja JSON → Obiekt
        User user = gson.fromJson(json, User.class);

        System.out.println("Name: " + user.name); // Alice
        System.out.println("Age: " + user.age);   // 25
    }
}