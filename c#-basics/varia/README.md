# c# varia
different c# notes

## UserName
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine($"Current User: {Environment.UserName}");          
        }
    }
}
```

## Environment.CurrentDirectory
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine($"Current User: {Environment.UserName}");
            string cwd = Environment.CurrentDirectory;
            Console.WriteLine($"CWD: {cwd}");
            Environment.CurrentDirectory = @"C:\csharpoutput";
            Console.WriteLine($"CWD: {Environment.CurrentDirectory}");
        }
    }
}
```

## Get Folder Path
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string desktopPath = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            Console.WriteLine(desktopPath);
        }      
    }
}
```
## Math
### Basic Operations
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Math.Min(1, 2)); //1
            Console.WriteLine(Math.Max(1, 2)); //2
            Console.WriteLine(Math.Pow(10, 2)); //100
            Console.WriteLine(Math.Abs(-10)); //10
        }        
    }
}
```
### Rounding numbers
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Math.Floor(20.3232345)); //20 (int)
            Console.WriteLine(Math.Ceiling(20.3232345)); //21 (int)
            double rounded = Math.Round(20.3232345); //its double!
            Console.WriteLine(Math.Round(20.3232345)); //20
            Console.WriteLine(Math.Round(20.3232345, 2)); // 20,32
        }        
    }
}
```
### DivRem
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            int result = Math.DivRem(9, 3, out int rem);
            Console.WriteLine(result); //3
            Console.WriteLine(rem); //0

            int result2 = Math.DivRem(10, 3, out int rem2);
            Console.WriteLine(result2); //3
            Console.WriteLine(rem2); //1
        }
    }
}
```

## TryParse
```cs
namespace ConsoleApp13
{
    class Program
    {
        static void Main(string[] args)
        {
            string okString = "1";
            string wrongString = "one";

            bool ok1 = int.TryParse(okString, out int parsed1);

            if (ok1)
            {
                Console.WriteLine(parsed1);
            }

            bool ok2 = int.TryParse(wrongString, out int parsed2);

            if (!ok2)
            {
                Console.WriteLine("Something went wrong");
            }
        }
    }
}
```

## Params in csharp
```cs
namespace ConsoleApp13
{
    class Program
    {
        static int Sum(params int[] numbers)
        {
            int _sum = 0;

            foreach(int n in numbers)
            {
                _sum += n;
            }

            return _sum;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Sum(1, 2, 3)); //6
            Console.WriteLine(Sum(1, 2, 3, 4, 5)); //15
        }
    }
}
```

## Callbacks in csharp
```cs
namespace ConsoleApp13
{
    class Program
    {
        static int WithCallback(int number, Func<int, int> cb)
        {
            return cb(number);
        }
        static void Main(string[] args)
        {
            Console.WriteLine(WithCallback(10, x => x + 42)); //52
            Console.WriteLine(WithCallback(10, x => x * x + 42)); //142
        }
    }
}
```