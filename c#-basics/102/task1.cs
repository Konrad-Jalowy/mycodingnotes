using System;
using System.Threading.Tasks;

namespace ConsoleApp18
{
    class Program
    {
        public static void write(char c)
        {
            int i = 1000;
            while (i-- > 0)
            {
                Console.Write(c);
            }
        }
        static void Main(string[] args)
        {
            
            Task.Factory.StartNew(() => write('.'));

            Task t = new(() => write('?'));
            t.Start();

            write('-');
        }
    }
}
