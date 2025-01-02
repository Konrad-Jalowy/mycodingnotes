namespace ConsoleApp15
{
    class Person
    {      
        public virtual string Name { get; set; }       
    }

    class Child : Person
    {
        private string _name;
        
        public override string Name
        {
            get
            {
                return _name;
            }
            set
            {
                if (!string.IsNullOrEmpty(value))
                {
                    _name = value;
                }
                else
                {
                    _name = "Unknown";
                }
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {           
            Person p1 = new Person() { Name = "" };
            Child c1 = new Child() { Name = "" };
            Console.WriteLine($"name {p1.Name}"); //name
            Console.WriteLine($"name {c1.Name}"); //name unknown
        }      
    }
}
