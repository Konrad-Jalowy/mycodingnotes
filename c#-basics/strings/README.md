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

## Interpolation
With $ symbol
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string firstName = "John";
            string lastName = "Doe";
            Console.WriteLine($"Fullname: {firstName} {lastName}");
        }
    }
}
```

## ToUpper(), ToLower()
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string firstName = "john";
            string lastName = "DOE";
            Console.WriteLine(firstName.ToUpper());
            Console.WriteLine(lastName.ToLower());
        }
    }
}
```

## Trim, TrimStart, TrimEnd
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string login = "   JohnD    ";
            Console.WriteLine(login.Trim());
            string firstName = "   John";
            Console.WriteLine(firstName.TrimStart());
            string lastName = "DOE   ";
            Console.WriteLine(lastName.TrimEnd());        
        }
    }
}
```

## Trim a char
Remember to use single quotes instead of double quotes for char type
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            char myChar = '0';
            Console.WriteLine(myChar);
            string time = "09";
            Console.WriteLine(time.TrimStart('0'));
            
        }
    }
}
```

## trim passing char array
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string time = "   09";
            Console.WriteLine(time.TrimStart(new char[] { '0', ' ' }));
        }
    }
}
```
## Null, empty, whitespace
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(String.IsNullOrEmpty(null)); //True
            Console.WriteLine(String.IsNullOrEmpty("")); //True
            Console.WriteLine(String.IsNullOrWhiteSpace(" ")); //True
            Console.WriteLine(String.IsNullOrWhiteSpace("")); //True
            Console.WriteLine(String.IsNullOrWhiteSpace(null)); //True
        }
    }
}
```

## Contains
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string s1 = "The quick brown fox jumps over the lazy dog";
            string s2 = "fox";
            if (s1.Contains(s2))
            {
                Console.WriteLine("Yes, s1 contains s2");
            }
        }
    }
}
```

## equals
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string s1 = "fox";
            string s2 = "fox";
            if (s1.Equals(s2))
            {
                Console.WriteLine("s1 === s2");
            }
        }
    }
}
```