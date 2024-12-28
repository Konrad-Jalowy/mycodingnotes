# C# collections
Notes on csharp collections.

## List
### Creating a list (and count property)
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1, 2, 3, 4, 5 };
            Console.WriteLine(numbers.Count); //5
        }
    }
}
```
### Adding to the end of a list
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1, 2, 3, 4, 5 };
            numbers.Add(6);
            numbers.Add(7);
            numbers.Add(8);
            Console.WriteLine(numbers.Count); //8
        }
    }
}
```
### List addrange
Range can be any IEnumerable
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1, 2, 3, 4, 5 };
            List<int> sublist = new List<int>() { 9, 10, 11 };
            numbers.Add(6);
            numbers.Add(7);
            numbers.Add(8);
            numbers.AddRange(sublist);
            Console.WriteLine(numbers.Count); //11
        }
    }
}
```
### Iterate over a list
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1, 2, 3, 4, 5 };
            foreach(int number in numbers)
            {
                Console.WriteLine(number);
            }
        }
    }
}
```
### Sorting a list
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 10, 2, 3, 6, 42, 5 };
            numbers.Sort();
            foreach(int number in numbers)
            {
                Console.WriteLine(number);
            }
        }
    }
}
```
### List binary search
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 10, 2, 3, 6, 42, 5 };
            numbers.Sort();
            Console.WriteLine(numbers.BinarySearch(5)); //2
            Console.WriteLine(numbers.BinarySearch(6)); //3
            Console.WriteLine(numbers.BinarySearch(41)); //-6
        }
    }
}
```