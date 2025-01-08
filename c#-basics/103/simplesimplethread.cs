namespace ConsoleApp18
{
    using System;
    using System.Threading;

    class Program
    {
        static void Main()
        {
            Thread thread1 = new Thread(PrintNumbers);
            Thread thread2 = new Thread(PrintNumbers);

            thread1.Start(); 
            thread2.Start(); 

            thread1.Join(); 
            thread2.Join(); 

            Console.WriteLine("Oba wątki zakończyły pracę.");
        }

        static void PrintNumbers()
        {
            for (int i = 1; i <= 5; i++)
            {
                Console.WriteLine($"Wątek {Thread.CurrentThread.ManagedThreadId} - Liczba: {i}");
                Thread.Sleep(500); 
            }
        }
    }
}
