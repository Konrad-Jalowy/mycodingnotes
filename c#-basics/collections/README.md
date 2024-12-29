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
### IndexOf
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
            Console.WriteLine(numbers.IndexOf(10)); //0
            Console.WriteLine(numbers.IndexOf(5)); //5
            Console.WriteLine(numbers.IndexOf(6)); //3
            Console.WriteLine(numbers.IndexOf(41)); //-1
        }
    }
}
```
### Contains
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
            Console.WriteLine(numbers.Contains(10)); //True
            Console.WriteLine(numbers.Contains(5)); //True
            Console.WriteLine(numbers.Contains(6)); //True
            Console.WriteLine(numbers.Contains(41)); //False
        }
    }
}
```
### List.Clear()
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
            numbers.Clear();
            Console.WriteLine(numbers.Count); //0
        }
    }
}
```
### List.Insert(idx, element)
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 4,5,6 };
            numbers.Insert(0, 3);
            numbers.Insert(0, 2);
            numbers.Insert(0, 1);
            numbers.Insert(0, 0);
            foreach (int number in numbers)
            {
                Console.WriteLine(number); //0,1,2,3,4,5,6
            }
        }
    }
}
```
### List.InsertRange(Idx, IEnumerable)
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1,2,3,7,8,9 };
            List<int> sublist = new List<int>() { 4, 5, 6 };
            numbers.InsertRange(3, sublist);
           
            foreach (int number in numbers)
            {
                Console.WriteLine(number); //1,2,3,4,5,6,7,8,9
            }
        }
    }
}
```
### List.TrueForAll
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1,2,3,7,8,9 };
            List<int> sublist = new List<int>() { 4, 5, 6 };
            bool numbersGreaterThanThree = numbers.TrueForAll(x => x > 3);
            Console.WriteLine(numbersGreaterThanThree); //False
            bool sublistGreaterThanThree = sublist.TrueForAll(x => x > 3);
            Console.WriteLine(sublistGreaterThanThree); //True
        }
    }
}
```