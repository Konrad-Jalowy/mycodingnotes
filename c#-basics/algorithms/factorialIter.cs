using System;
namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(GetFactorial(-2)); //-1
            Console.WriteLine(GetFactorial(-1)); //-1
            Console.WriteLine(GetFactorial(0)); //1
            Console.WriteLine(GetFactorial(1)); //1
            Console.WriteLine(GetFactorial(2)); //2
            Console.WriteLine(GetFactorial(3)); //6
            Console.WriteLine(GetFactorial(4)); //24

        }
        private static long GetFactorial(int number)
        {
            int result = number;

            if(number < 0)
            {
                return -1;
            }

            if (number == 1 || number == 0)
            {
                return 1;
            }

            while(number > 1)
            {
                number--;
                result *= number;
            }

            return result;

        }
    }    
}
