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
