using System;
using System.Threading;
namespace ConsoleApp15
{
    class Storage
    {
        private int[] _numbers = new int[] { 1, 2, 3, 4, 5 };

        public int this[int index]
        {
            set
            {
                this._numbers[index] = value;
            }
            get
            {
                return this._numbers[index];
            }
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hi!");

            Storage storage1 = new Storage();
            Console.WriteLine(storage1[0]); //1
            Console.WriteLine(storage1[4]); //5
            storage1[4] = 6;
            Console.WriteLine(storage1[4]); //6
        }      
    }
}
