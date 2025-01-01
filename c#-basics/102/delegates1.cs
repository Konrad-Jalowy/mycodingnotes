using System;
using System.Threading;
namespace ConsoleApp15
{
    
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hi!");

            WelcomePerson hiDelegate = SayHi;
            WelcomePerson helloDelegate = new WelcomePerson(SayHello); //older way

            hiDelegate("John"); //Hi John
            helloDelegate("Jane"); //Hello Jane
           
        }

        public delegate void WelcomePerson(string name);

        public static void SayHi(string name)
        {
            Console.WriteLine($"Hi {name}");
        }

        public static void SayHello(string name)
        {
            Console.WriteLine($"Hello {name}");
        }

    }
}
