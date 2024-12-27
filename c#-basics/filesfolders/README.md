# C# files and folders notes

## printing CWD
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string path = Directory.GetCurrentDirectory();
            Console.WriteLine("The current directory is {0}", path);
        }
    }
}
```

## Check if directory exists
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
         
            if (!Directory.Exists("./somefolder"))
            {
                Console.WriteLine("Doesnt exist");
            }
        }
    }
}
```