using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime today = DateTime.Now;
            DateTime newYear = new DateTime(today.Year + 1, 1, 1);

            TimeSpan ts = newYear.Subtract(today);
            Console.WriteLine(ts.Days); //2
            Console.WriteLine(ts.Hours); //13
            Console.WriteLine(ts.Minutes); //16
            Console.WriteLine(ts.Seconds); //33
        }        
    }
}
