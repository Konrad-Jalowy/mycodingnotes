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

## Some basics
```cs
namespace ConsoleApp15
{
    class Student
    {
        public string Name { get; set; }

        public Student(string name)
        {
            Name = name;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Student std1 = new Student("John Doe");
            Console.WriteLine(std1.Name);
            std1.Name = "Jane Doe";
            Console.WriteLine(std1.Name);
        }
    }
}
```

## Generic class basics
```cs
namespace ConsoleApp15
{
    class GenericObj<T>
    {
        public T Data { get; set; }

        public GenericObj(T data)
        {
            Data = data;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hi!");

            GenericObj<string> obj1 = new GenericObj<string>("Hello World");
            GenericObj<int> obj2 = new GenericObj<int>(123);
            GenericObj<bool> obj3 = new GenericObj<bool>(true);

            Console.WriteLine(obj1.Data);
            Console.WriteLine(obj2.Data);
            Console.WriteLine(obj3.Data);
        }
    }
}
```

## Value types only
It also excludes strings
```cs
class GenericObj<T> where T: struct
    {
        public T Data { get; set; }

        public GenericObj(T data)
        {
            Data = data;
        }
    }
```

## Object initializers
```cs
namespace ConsoleApp15
{
    class Employee
    {
        public string firstName;
        public string lastName;
        public int age;
        public double money;
        public int id;

        public override string ToString()
        {
            return $"id: {id} {firstName} {lastName} {age} years old {money}$";
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hi!");

            Employee emp1 = new Employee() { firstName = "John", lastName = "Doe", age = 30, id = 1, money = 1500 };
            Employee emp2 = new Employee() { firstName = "Jane", lastName = "Doe", age = 20, id = 2, money = 2500 };

            Console.WriteLine(emp1.ToString()); //id: 1 John Doe 30 years old 1500$
            Console.WriteLine(emp2.ToString()); //id: 2 Jane Doe 20 years old 2500$
        }      
    }
}
```

## Indexers 
```cs
using System;
using System.Threading;
namespace ConsoleApp15
{
    class Storage
    {
        private int[] _numbers = new int[] { 1, 2, 3, 4, 5 };

        public int this[int index]
        {
            set
            {
                this._numbers[index] = value;
            }
            get
            {
                return this._numbers[index];
            }
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hi!");

            Storage storage1 = new Storage();
            Console.WriteLine(storage1[0]); //1
            Console.WriteLine(storage1[4]); //5
            storage1[4] = 6;
            Console.WriteLine(storage1[4]); //6
        }      
    }
}
```

## Method hiding vs method overriding
Example I found:
```cs
public class BaseClass
{
  public void WriteNum()
  {
    Console.WriteLine(12);
  }
  public virtual void WriteStr()
  {
    Console.WriteLine("abc");
  }
}

public class DerivedClass : BaseClass
{
  public new void WriteNum()
  {
    Console.WriteLine(42);
  }
  public override void WriteStr()
  {
    Console.WriteLine("xyz");
  }
}
/* ... */
BaseClass isReallyBase = new BaseClass();
BaseClass isReallyDerived = new DerivedClass();
DerivedClass isClearlyDerived = new DerivedClass();

isReallyBase.WriteNum(); // writes 12
isReallyBase.WriteStr(); // writes abc
isReallyDerived.WriteNum(); // writes 12
isReallyDerived.WriteStr(); // writes xyz
isClearlyDerived.WriteNum(); // writes 42
isClearlyDerived.writeStr(); // writes xyz
```