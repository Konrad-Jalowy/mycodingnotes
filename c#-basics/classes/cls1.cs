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