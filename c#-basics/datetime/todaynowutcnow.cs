using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime today = DateTime.Today;
            Console.WriteLine(today.ToString()); //28.12.2024 00:00:00

            DateTime now = DateTime.Now;
            Console.WriteLine(now.ToString()); //28.12.2024 13:46:41

            DateTime utcNow = DateTime.UtcNow;
            Console.WriteLine(utcNow.ToString()); //28.12.2024 12:47:27
        }
    }
}
