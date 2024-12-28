using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime now = DateTime.Now;
            Console.WriteLine($"Time:>{now.Hour}:{now.Minute}:{now.Second}"); //Time:>13:50:47
        }
    }
}