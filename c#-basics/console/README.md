# C# Console 
c# console notes

## Environment.NewLine, Console.Write
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Starting App!" + Environment.NewLine);
            Console.Write("Hi!" + Environment.NewLine);
            Console.Write("Exiting App!" + Environment.NewLine);
        }
    }
}
```
## Normal Way (Console.WriteLine)
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Starting App!");
            Console.WriteLine("Hi!");
            Console.WriteLine("Exiting App!");
        }
    }
}
```
## Console and colors
you can always google them
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.BackgroundColor = ConsoleColor.Blue;
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine("White on blue.");
            Console.WriteLine("Another line.");
            Console.ResetColor();
        }
    }
}
```

## Readline
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string userInput = Console.ReadLine();
            Console.WriteLine(userInput);
        }
    }
}
```