using System;
using System.Threading;
namespace ConsoleApp14
{
    class Program
    {
        static string Name = "john";
        static void Main(string[] args)
        {
            
            Thread th1 = new Thread(AddDoe);
            th1.Start();
  
            Thread th2 = new Thread(Capitalize);           
            th2.Start();

            Console.WriteLine("Before");
            th1.Join();
            th2.Join();
            Console.WriteLine("All threads finished");
            Console.WriteLine(Name);
        }

        static void AddDoe()
        {
            lock(Name)
            {
                Name = Name + " Doe";
            }              
        }

        static void Capitalize()
        {
            lock(Name)
            {
                Name = "John";
            }           
        }
    }
}