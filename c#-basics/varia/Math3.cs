using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            int result = Math.DivRem(9, 3, out int rem);
            Console.WriteLine(result); //3
            Console.WriteLine(rem); //0

            int result2 = Math.DivRem(10, 3, out int rem2);
            Console.WriteLine(result2); //3
            Console.WriteLine(rem2); //1
        }
    }
}
