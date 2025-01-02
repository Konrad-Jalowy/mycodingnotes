using System;
using System.Threading;
namespace ConsoleApp15
{
    class Program
    {
        static void Main(string[] args)
        {
            int age = 18;
            GetOlder(ref age);
            Console.WriteLine(age); //19
        }
        public static void GetOlder(ref int age)
        {
            age++;
        }
    }
}
