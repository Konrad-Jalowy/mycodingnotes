using System;
using System.IO;

class Program
{
    static void Main()
    {
        string filePath = "source.txt";

        // Utwórz plik źródłowy
        File.WriteAllText(filePath, "Przykładowy tekst do skopiowania!");

        // Kopiowanie z FileStream do MemoryStream
        using (FileStream sourceStream = new FileStream(filePath, FileMode.Open))
        using (MemoryStream memoryStream = new MemoryStream())
        {
            sourceStream.CopyTo(memoryStream);
            memoryStream.Seek(0, SeekOrigin.Begin); // Resetuj wskaźnik

            string copiedContent = System.Text.Encoding.UTF8.GetString(memoryStream.ToArray());
            Console.WriteLine($"Skopiowana zawartość: {copiedContent}");
        }
    }
}