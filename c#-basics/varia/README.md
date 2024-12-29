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