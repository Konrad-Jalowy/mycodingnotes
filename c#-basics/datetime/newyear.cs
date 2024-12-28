using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime newYear = new DateTime(2025, 1, 1);
            string hour = newYear.Hour.ToString().PadLeft(2, '0');
            string minute = newYear.Minute.ToString().PadLeft(2, '0');
            string second = newYear.Second.ToString().PadLeft(2, '0');
            Console.WriteLine($"Time:>{hour}:{minute}:{second}"); //Time:>00:00:00
            Console.WriteLine($"Date:{newYear.Year}-{newYear.Month}-{newYear.Day}"); //Date:2025-1-1
        }
    }
}