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
### List.Reverse()
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1,2,3};
            numbers.Reverse();
            foreach(int num in numbers)
            {
                Console.WriteLine(num); //3,2,1
            }
        }
    }
}
```
### List.Find
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1,2,3};
            int notOdd = numbers.Find(x => x % 2 == 0);
            Console.WriteLine(notOdd); //2
        }
    }
}
```

### List.ForEach
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            
            List<string> names = new List<string>();
            names.Add("Bruce");
            names.Add("Alfred");
            names.Add("Tim");
            names.Add("Richard");
            names.ForEach(Print);

            void Print(string s)
            {
                Console.WriteLine(s);
            }
        }
      
    }
      
}
```
### List of objects of some class
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp12
{
    class Employee
    {
        public int EmpID { get; set; }
        public string EmpName { get; set; }
        public string Job { get; set; }
        public string City { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Employee> employees = new List<Employee>()
            {
                new Employee() { EmpID = 101, EmpName = "John Doe", Job = "Developer", City = "New York" },
                new Employee() { EmpID = 102, EmpName = "Jane Doe", Job = "Manager", City = "New York" },
                new Employee() { EmpID = 103, EmpName = "Jim Doe", Job = "Manager", City = "London" },
                new Employee() { EmpID = 104, EmpName = "Janet Doe", Job = "Developer", City = "Warsaw" },
                new Employee() { EmpID = 105, EmpName = "Jane Json", Job = "Manager", City = "Warsaw" },
                new Employee() { EmpID = 106, EmpName = "Jim Xml", Job = "Developer", City = "London" },
            };

            Console.WriteLine(employees.Count); //6

        }
        
    }    
}
```
## Stack
### Basic operations
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string msg = "hello world!";
            Stack<char> characters = new Stack<char>();
            foreach(char c in msg)
            {
                characters.Push(c);
            }
            Console.WriteLine(characters.Count); //12
            Console.WriteLine(characters.Peek()); //!
            Console.WriteLine(characters.Contains('w')); //True
            Console.WriteLine(characters.Contains('W')); //False
            Console.WriteLine(characters.Pop()); //!
            Console.WriteLine(characters.Count); //11
        }
        
    }
}
```
### TryPeek TryPop
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Stack<char> characters = new Stack<char>();
            if(characters.TryPeek(out char lastOne))
            {
                Console.WriteLine(lastOne);
            } else
            {
                Console.WriteLine("Looks like the stack is empty...");
            }

            string msg = "abc!";        
            
            foreach(char c in msg)
            {
                characters.Push(c);
            }

            if(characters.TryPop(out char poppedOne))
            {
                Console.WriteLine($"Popped char : {poppedOne}");
            }            
        }
        
    }
}
```
## Dictionary
### Creating and reading dictionary
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {

            Dictionary<int, string> people = new Dictionary<int, string>()
            {
                {1, "John Doe" },
                {2, "Jane Doe" },
                {3, "Jim Doe" }
            };
            foreach(KeyValuePair<int, string> item in people)
            {
                Console.WriteLine(item.Key + " : " + item.Value);
            }
        }
      
    }
      
}
```
### By key name
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<int, string> people = new Dictionary<int, string>()
            {
                {1, "John Doe" },
                {2, "Jane Doe" },
                {3, "Jim Doe" }
            };

            Console.WriteLine(people[1]); //John Doe
            Console.WriteLine(people[2]); //Jane Doe
            Console.WriteLine(people[3]); //Jim Doe
        }     
    }    
}
```
### Using keys
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<int, string> people = new Dictionary<int, string>()
            {
                {1, "John Doe" },
                {2, "Jane Doe" },
                {3, "Jim Doe" }
            };

            Dictionary<int, string>.KeyCollection keys = people.Keys;

            foreach(int k in keys)
            {
                Console.WriteLine(people[k]);
            }
        }     
    }    
}
```
### Add, Remove
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<int, string> people = new Dictionary<int, string>()
            {
                {1, "John Doe" },
                {2, "Jane Doe" },
                {3, "Jim Doe" }
            };

            people.Remove(3);
            people.Add(3, "John Doe");

            Dictionary<int, string>.KeyCollection keys = people.Keys;

            foreach(int k in keys)
            {
                Console.WriteLine(people[k]);
            }
        }     
    }    
}
```
### ContainsKey, ContainsValue
```cs
using System;
using System.Collections.Generic;
namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<int, string> people = new Dictionary<int, string>()
            {
                {1, "John Doe" },
                {2, "Jane Doe" },
                {3, "Jim Doe" }
            };

            Console.WriteLine(people.ContainsKey(3)); //True
            Console.WriteLine(people.ContainsValue("John Doe")); //True
        }     
    }    
}
```