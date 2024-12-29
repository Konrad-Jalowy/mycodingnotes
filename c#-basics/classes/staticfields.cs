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