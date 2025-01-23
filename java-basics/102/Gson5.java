import com.google.gson.Gson;

class Address {
    String city;
    String country;
}

class User {
    String name;
    Address address;
}

public class Gson5 {
    public static void main(String[] args) {
        String json = "{\"name\":\"Alice\",\"address\":{\"city\":\"Warsaw\",\"country\":\"Poland\"}}";

        Gson gson = new Gson();
        User user = gson.fromJson(json, User.class);

        System.out.println(user.name);             // Alice
        System.out.println(user.address.city);     // Warsaw
        System.out.println(user.address.country);  // Poland
    }
}
