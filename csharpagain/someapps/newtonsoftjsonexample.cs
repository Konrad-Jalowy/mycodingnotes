using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

class Program
{
    static void Main()
    {
        string json = @"{
            'Alice': { 'Math': 90, 'English': 85 },
            'Bob': { 'Math': 80, 'Science': 88 }
        }";

        // Parsowanie jako dynamiczny obiekt
        var dynamicJson = JsonConvert.DeserializeObject<JObject>(json);

        foreach (var student in dynamicJson)
        {
            Console.WriteLine($"Uczeń: {student.Key}");
            foreach (var subject in student.Value)
            {
                Console.WriteLine($"  Przedmiot: {subject.Path}, Ocena: {subject.First}");
            }
        }
    }
}

