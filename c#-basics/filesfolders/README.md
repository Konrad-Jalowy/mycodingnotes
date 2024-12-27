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

## Change CWD
### First way
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
            string target = @"C:\somepath";
            if (!Directory.Exists(target))
            {
                Directory.CreateDirectory(target);
            }
            Environment.CurrentDirectory = (target);
            Console.WriteLine(Directory.GetCurrentDirectory());
        }
    }
}
```
### Second way
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
            string target = @"C:\somepath";
            if (!Directory.Exists(target))
            {
                Directory.CreateDirectory(target);
            }
            Directory.SetCurrentDirectory(target);
            Console.WriteLine(Directory.GetCurrentDirectory());
        }
    }
}
```

## getfiles
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

            string target = @"C:\somepath";

            if (!Directory.Exists(target))
            {
                Directory.CreateDirectory(target);
            }

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string[] files = Directory.GetFiles(cwd, "*");

            foreach (string file in files)
            {
                Console.WriteLine(file);
            }
        }
    }
}
```
## get filename
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

            string target = @"C:\somepath";

            if (!Directory.Exists(target))
            {
                Directory.CreateDirectory(target);
            }

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string[] files = Directory.GetFiles(cwd, "*");

            foreach (string file in files)
            {
                Console.WriteLine(Path.GetFileName(file));
            }
        }
    }
}
```

## StreamWriter writing to a file
```cs
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string[] lines = { "First line", "Second line", "Third line" };

            using (StreamWriter outputFile = new StreamWriter(Path.Combine(cwd, "WriteLines.txt")))
            {
                foreach (string line in lines)
                    outputFile.WriteLine(line);
            }
        }
    
    }
}
```

## streamwriter append to a file
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

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string[] lines = { "First line", "Second line", "Third line" };

            using (StreamWriter outputFile = new StreamWriter(Path.Combine(cwd, "WriteLines.txt"), append: true))
            {
                foreach (string line in lines)
                    outputFile.WriteLine(line);
            }
        }
    
    }
}
```
## exists
and interpolation in c#
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

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string path = Path.Combine(cwd, "WriteLines.txt");

            if (File.Exists(path))
            {
                Console.WriteLine($"Working directory: {cwd}");
                Console.WriteLine($"File {Path.GetFileName(path)} exists!");
            }
        }
    
    }
}
```