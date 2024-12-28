using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(String.IsNullOrEmpty(null)); //True
            Console.WriteLine(String.IsNullOrEmpty("")); //True
            Console.WriteLine(String.IsNullOrWhiteSpace(" ")); //True
            Console.WriteLine(String.IsNullOrWhiteSpace("")); //True
            Console.WriteLine(String.IsNullOrWhiteSpace(null)); //True
        }
    }
}
