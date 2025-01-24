using System.Collections.Generic;
using System.Text.Json;

class Program
{
    static void Main()
    {
        // Tworzenie słownika
        Dictionary<string, int> ageDict = new Dictionary<string, int>
        {
            { "Alice", 25 },
            { "Bob", 30 },
            { "Charlie", 35 }
        };

        // Serializacja słownika do JSON
        string json = JsonSerializer.Serialize(ageDict);

        Console.WriteLine("Słownik jako JSON:");
        Console.WriteLine(json);

        // Deserializacja z JSON do słownika
        Dictionary<string, int> deserializedDict = JsonSerializer.Deserialize<Dictionary<string, int>>(json);

        Console.WriteLine("\nOdszyfrowany słownik:");
        foreach (var entry in deserializedDict)
        {
            Console.WriteLine($"Klucz: {entry.Key}, Wartość: {entry.Value}");
        }
    }
}