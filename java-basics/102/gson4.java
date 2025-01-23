import com.google.gson.Gson;
import com.google.gson.annotations.SerializedName;

class User {
    @SerializedName("full_name")
    String name;

    @SerializedName("user_age")
    int age;
}

public class gson4 {
    public static void main(String[] args) {
        String json = "{\"full_name\": \"Alice\", \"user_age\": 25}";

        Gson gson = new Gson();

        User user = gson.fromJson(json, User.class);

        System.out.println("Name: " + user.name); // Alice
        System.out.println("Age: " + user.age);   // 25
    }
}
