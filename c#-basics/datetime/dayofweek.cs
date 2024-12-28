using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime newYear = new DateTime(2025, 1, 1);
            Console.WriteLine($"New Year will be {newYear.DayOfWeek}");
        }
    }
}
