using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime today = DateTime.Now;
            DateTime newYear = new DateTime(today.Year + 1, 1, 1);

            Console.WriteLine(today.CompareTo(newYear)); //-1
            Console.WriteLine(today.CompareTo(today)); //0
            Console.WriteLine(newYear.CompareTo(today)); //1
        }        
    }
}
