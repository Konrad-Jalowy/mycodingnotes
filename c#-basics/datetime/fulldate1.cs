using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime now = DateTime.Now;
            string hour = now.Hour.ToString().PadLeft(2, '0');
            string minute = now.Minute.ToString().PadLeft(2, '0');
            string second = now.Second.ToString().PadLeft(2, '0');
            Console.WriteLine($"Time:>{hour}:{minute}:{second}"); //Time:>13:56:56
            Console.WriteLine($"Date:{now.Year}-{now.Month}-{now.Day}"); //Date:2024-12-28
        }
    }
}
