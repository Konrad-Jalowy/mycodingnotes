using System;
using System.IO;

class Program
{
    static void Main()
    {
        using (StreamReader reader = new StreamReader("example.txt"))
        {
            string content = reader.ReadToEnd();
            Console.WriteLine(content);
        }
    }
}
