using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Math.Floor(20.3232345)); //20 (int)
            Console.WriteLine(Math.Ceiling(20.3232345)); //21 (int)
            double rounded = Math.Round(20.3232345); //its double!
            Console.WriteLine(Math.Round(20.3232345)); //20
            Console.WriteLine(Math.Round(20.3232345, 2)); // 20,32
        }        
    }
}
