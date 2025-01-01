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
