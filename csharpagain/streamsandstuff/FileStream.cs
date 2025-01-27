using System;
using System.IO;

class Program
{
    static void Main()
    {
        using (FileStream fs = new FileStream("example.txt", FileMode.Open))
        {
            byte[] buffer = new byte[fs.Length];
            fs.Read(buffer, 0, buffer.Length);
            string content = System.Text.Encoding.UTF8.GetString(buffer);
            Console.WriteLine(content);
        }
    }
}