namespace ConsoleApp13
{
    class Program
    {
        static int WithCallback(int number, Func<int, int> cb)
        {
            return cb(number);
        }
        static void Main(string[] args)
        {
            Console.WriteLine(WithCallback(10, x => x + 42)); //52
            Console.WriteLine(WithCallback(10, x => x * x + 42)); //142
        }
    }
}
