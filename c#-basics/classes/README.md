# csharp classes 
notes on csharp classes

## constructor + fields
```cs
namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {          
            Person p1 = new Person("John", "Doe");        
            Console.WriteLine(p1.FirstName); //John
            Console.WriteLine(p1.LastName); //Doe
        }
    }
    public class Person
    {
        public string LastName { get; set; }
        public string FirstName { get; set; }

        public Person(string first, string last)
        {
            FirstName = first;
            LastName = last;
        }
    }
}
```
## ToString override
```cs
using System;

namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {          
            Person p1 = new Person("John", "Doe");        
            Console.WriteLine(p1.ToString()); //John Doe
        }
    }
    public class Person
    {
        public string LastName { get; set; }
        public string FirstName { get; set; }

        public Person(string first, string last)
        {
            FirstName = first;
            LastName = last;
        }

        public override string ToString()
        {
            return $"{this.FirstName} {this.LastName}";
        }
    }
}
```
## Multiple constructors
```cs
using System;

namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {          
            Person p1 = new Person("John", "Doe");        
            Console.WriteLine(p1.ToString()); //John Doe
            Person p2 = new Person("Jane Doe");
            Console.WriteLine(p2.ToString()); //Jane Doe           
        }
    }
    public class Person
    {
        public string LastName { get; set; }
        public string FirstName { get; set; }

        public Person(string first, string last)
        {
            FirstName = first;
            LastName = last;
        }

        public Person(string fullname)
        {
            string[] names = fullname.Split(' ');
            FirstName = names[0];
            LastName = names[1];
        }

        public override string ToString()
        {
            return $"{this.FirstName} {this.LastName}";
        }
    }
}
```

## Static method in  CS
```cs
namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Calculator.Add(2, 2)); //4
                    
        }
    }
    class Calculator
    {
        public static int Add(int num1,  int num2)
        {
            return num1 + num2;
        }
    }
}
```

## Static fields
```cs
using System;

namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Person.instances); //0
            Person p1 = new Person("John", "Doe");
            Console.WriteLine(p1.FirstName); //John
            Console.WriteLine(p1.LastName); //Doe
            Console.WriteLine(Person.instances); //1
        }
    }
    public class Person
    {
        public string LastName { get; set; }
        public string FirstName { get; set; }
        public static int instances = 0;

        public Person(string first, string last)
        {
            FirstName = first;
            LastName = last;
            instances++;
        }

        ~Person()
        {
            instances--;
        }
    }
}
```