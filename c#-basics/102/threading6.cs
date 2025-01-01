using System;
using System.Threading;
namespace ConsoleApp14
{
    class Program
    {
        static void Main(string[] args)
        {
            ThreadStart threadStart1 = new ThreadStart(CountUp);
            Thread th1 = new Thread(threadStart1);
            th1.Start();

            ThreadStart threadStart2 = new ThreadStart(CountDown);
            Thread th2 = new Thread(threadStart2);
            th2.Start();

            Console.WriteLine("Believe it or not ill run before those threads are finished");
            th1.Join();
            th2.Join();
            Console.WriteLine("Ill run when th1 and th2 are finished, not before that...");
            
        }
     
        static void CountUp()
        {
            for(int i = 0; i <= 10; i++)
            {
                Console.WriteLine(i);
                Thread.Sleep(10);
            }
            Thread.Sleep(1000);
        }

        static void CountDown()
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
