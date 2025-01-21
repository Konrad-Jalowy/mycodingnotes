using System;

namespace ConsoleApp20
{

    public class User
    {
        public string Name { get; set; }
        public int? Age { get; set; }
    }

    class Program
    {
        static void Main()
        {
            User user = new User { Name = "Alice", Age = 25 };

            if (user is { Name: { Length: > 0 }, Age: >= 18 })
            {
                Console.WriteLine("Poprawny użytkownik.");
            }
            else
            {
                Console.WriteLine("Niepoprawny użytkownik.");
            }
        }
    }
}