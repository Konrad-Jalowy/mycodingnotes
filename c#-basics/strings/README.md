# C# Strings
Notes on Strings in C#

## Paths
Paths always with @ symbol, so that \ is not escape character
```cs
using System;
using System.IO;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World");
            string path = @":c\csharpoutput";
            Console.WriteLine(Directory.Exists(path));
        }
    }
}
```