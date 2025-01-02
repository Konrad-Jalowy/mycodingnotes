namespace ConsoleApp15
{
    class Person
    {
       
        public string Name { get; set; }

        public Person(string name)
        {
            Name = name;
        }

    }

    class Child : Person
    {
        public string ParentName { get; set; }

        public Child(string name, string parentName): base(name)
        {
            ParentName = parentName;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Person p1 = new("John Doe");
            Child c1 = new("Jane Doe", "John Doe");

            Console.WriteLine(p1.Name);
            Console.WriteLine($"{c1.Name}, child of {c1.ParentName}");        
        }      
    }
}
