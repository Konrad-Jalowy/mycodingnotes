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

## path combine
remember not to use your own separators
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
            string basePath = Directory.GetCurrentDirectory();
            string directory = "somefolder";

            if (Directory.Exists(Path.Combine(basePath, directory)))
            {
                Console.WriteLine("Directory exists!");
            }
        }
    }
}
```

## create directory
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
            string basePath = Directory.GetCurrentDirectory();
            string directory = @"somefolder2";
            string path = Path.Combine(basePath, directory);
            Console.WriteLine(path);

            if (!Directory.Exists(path))
            {
                Console.WriteLine("Creating directory!");
                Directory.CreateDirectory(path);
            }
        }
    }
}
```