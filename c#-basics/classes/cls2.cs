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
