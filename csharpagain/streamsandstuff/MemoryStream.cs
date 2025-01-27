using System;
using System.IO;

class Program
{
    static void Main()
    {
        using (MemoryStream ms = new MemoryStream())
        {
            // Zapisz dane do strumienia w pamięci
            byte[] data = System.Text.Encoding.UTF8.GetBytes("Hello, MemoryStream!");
            ms.Write(data, 0, data.Length);

            // Przeczytaj dane z pamięci
            ms.Seek(0, SeekOrigin.Begin); // Cofnij wskaźnik do początku
            byte[] buffer = new byte[ms.Length];
            ms.Read(buffer, 0, buffer.Length);

            string content = System.Text.Encoding.UTF8.GetString(buffer);
            Console.WriteLine(content);
        }
    }
}