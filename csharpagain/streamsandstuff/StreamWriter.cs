using System;
using System.IO;

class Program
{
    static void Main()
    {
        using (StreamWriter writer = new StreamWriter("example.txt"))
        {
            writer.WriteLine("Cześć, Streamy w C#!");
        }
        Console.WriteLine("Zapisano do pliku.");
    }
}
