using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime today = DateTime.Today;
            int daysInCurrYear = DateTime.IsLeapYear(today.Year) ? 366 : 365;
            int currDayOfYear = today.DayOfYear;
            int daysLeft = daysInCurrYear - currDayOfYear;

            Console.WriteLine($"New Years Eve in {daysLeft} days.");
            Console.WriteLine($"New Year {today.Year + 1} in {daysLeft + 1} days.");              
        }
    }
}
