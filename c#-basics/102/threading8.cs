using System;
using System.Threading;
namespace ConsoleApp14
{
    class Program
    {
        static void Main(string[] args)
        {
            ThreadPool.QueueUserWorkItem(CountUp);
            ThreadPool.QueueUserWorkItem(CountDown);
            Thread.Sleep(3000);
            Console.WriteLine("When main thread dies, threadpool items also die no matter finished or not...");
            
        }
     
        static void CountUp(Object stateInfo)
        {
            for(int i = 0; i <= 10; i++)
            {
                Console.WriteLine(i);
                Thread.Sleep(10);
            }
            Thread.Sleep(1000);
        }

        static void CountDown(Object stateInfo)
        {
            for (int i = 20; i >= 11; i--)
            {
                Console.WriteLine(i);
                Thread.Sleep(10);
            }
            Thread.Sleep(1000);
        }
    }
}
