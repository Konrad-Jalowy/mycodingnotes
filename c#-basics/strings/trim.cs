using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string login = "   JohnD    ";
            Console.WriteLine(login.Trim());
            string firstName = "   John";
            Console.WriteLine(firstName.TrimStart());
            string lastName = "DOE   ";
            Console.WriteLine(lastName.TrimEnd());        
        }
    }
}