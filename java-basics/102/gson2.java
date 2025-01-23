import com.google.gson.Gson;

class User {
    String name;
    int age;
}

public class gson2 {
    public static void main(String[] args) {
        User user = new User();
        user.name = "Bob";
        user.age = 30;

        // Tworzymy obiekt Gson
        Gson gson = new Gson();

        // Konwersja Obiekt → JSON
        String json = gson.toJson(user);

        System.out.println(json); // {"name":"Bob","age":30}
    }
}
