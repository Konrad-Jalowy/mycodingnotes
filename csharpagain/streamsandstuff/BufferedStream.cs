using System;
using System.IO;

class Program
{
    static void Main()
    {
        string filePath = "bufferedExample.txt";

        // Zapis z buforowaniem
        using (FileStream fileStream = new FileStream(filePath, FileMode.Create))
        using (BufferedStream bufferedStream = new BufferedStream(fileStream, 8192)) // Bufor 8 KB
        using (StreamWriter writer = new StreamWriter(bufferedStream))
        {
            writer.WriteLine("Dane zapisane z użyciem BufferedStream.");
        }

        // Odczyt z buforowaniem
        using (FileStream fileStream = new FileStream(filePath, FileMode.Open))
        using (BufferedStream bufferedStream = new BufferedStream(fileStream, 8192))
        using (StreamReader reader = new StreamReader(bufferedStream))
        {
            string content = reader.ReadToEnd();
            Console.WriteLine($"Odczytana zawartość: {content}");
        }
    }
}

