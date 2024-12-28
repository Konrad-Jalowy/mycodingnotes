using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime newYear = new DateTime(2025, 1, 1);
            Console.WriteLine($"New Year will be {newYear.DayOfWeek}");
            bool leap = DateTime.IsLeapYear(newYear.Year);
            if (leap)
            {
                Console.WriteLine($"New Year {newYear.Year} will be leap Year and have 366 days");
            } else
            {
                Console.WriteLine($"New Year {newYear.Year} will have 365 days");
            }
        }
    }
}