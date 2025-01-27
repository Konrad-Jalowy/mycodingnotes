using System;
using System.IO;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        string filePath = "asyncExample.txt";
        string content = "Przykład asynchronicznego zapisu i odczytu.";

        // Asynchroniczny zapis
        await using (FileStream fs = new FileStream(filePath, FileMode.Create, FileAccess.Write, FileShare.None, 4096, true))
        {
            byte[] data = Encoding.UTF8.GetBytes(content);
            await fs.WriteAsync(data, 0, data.Length);
        }

        // Asynchroniczny odczyt
        await using (FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.Read, 4096, true))
        {
            byte[] buffer = new byte[fs.Length];
            await fs.ReadAsync(buffer, 0, buffer.Length);
            string readContent = Encoding.UTF8.GetString(buffer);
            Console.WriteLine($"Odczytana zawartość: {readContent}");
        }
    }
}
