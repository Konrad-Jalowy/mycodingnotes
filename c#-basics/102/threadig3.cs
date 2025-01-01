using System;
using System.Threading;
namespace ConsoleApp14
{
    class Program
    {
        static void Main(string[] args)
        {
            ThreadStart threadStart1 = new ThreadStart(Hello);
            Thread th1 = new Thread(threadStart1);
            th1.Start();
        }

        static void Hello()
        {
            Console.WriteLine("Hello world from thread");
        }
    }
}
