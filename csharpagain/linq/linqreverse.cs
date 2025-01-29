using System;
using System.Linq;

class Program
{
    static void Main()
    {
        string text = "Hello, LINQ!";
        var reversed = new string(text.Reverse().ToArray());

        Console.WriteLine($"Odwrócony tekst: {reversed}");
    }
}
