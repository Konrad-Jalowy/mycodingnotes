namespace ConsoleApp13
{
    class Program
    {
        static int Sum(params int[] numbers)
        {
            int _sum = 0;

            foreach(int n in numbers)
            {
                _sum += n;
            }

            return _sum;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Sum(1, 2, 3)); //6
            Console.WriteLine(Sum(1, 2, 3, 4, 5)); //15
        }
    }
}
