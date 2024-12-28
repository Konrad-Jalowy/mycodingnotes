using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime now = DateTime.Now;
            Console.WriteLine(now.ToString("dd-MM-yyyy")); //28-12-2024
            Console.WriteLine(now.ToString("dd MMMM yyyy")); //28 grudnia 2024
            Console.WriteLine(now.ToString("(ddd) dd MMMM yyyy")); //(sob.) 28 grudnia 2024
            Console.WriteLine(now.ToString("HH:mm:ss")); //17:58:33
            Console.WriteLine(now.ToString("hh:mm:ss")); //05:58:54
        }
    }
}
