import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.Map;

public class MapSerializationExample {
    public static void main(String[] args) {
        // Tworzenie mapy
        Map<String, Integer> ageMap = new HashMap<>();
        ageMap.put("Alice", 25);
        ageMap.put("Bob", 30);
        ageMap.put("Charlie", 35);

        // Tworzenie obiektu Gson
        Gson gson = new Gson();

        // Serializacja mapy do JSON
        String json = gson.toJson(ageMap);

        System.out.println("Mapa jako JSON:");
        System.out.println(json);

        // Deserializacja z JSON do mapy
        Type mapType = new TypeToken<Map<String, Integer>>() {}.getType();
        Map<String, Integer> deserializedMap = gson.fromJson(json, mapType);

        System.out.println("\nOdszyfrowana mapa:");
        for (Map.Entry<String, Integer> entry : deserializedMap.entrySet()) {
            System.out.println("Klucz: " + entry.getKey() + ", Wartość: " + entry.getValue());
        }
    }
}
