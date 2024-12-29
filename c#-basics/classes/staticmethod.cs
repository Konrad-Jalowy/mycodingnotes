namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Calculator.Add(2, 2)); //4
                    
        }
    }
    class Calculator
    {
        public static int Add(int num1,  int num2)
        {
            return num1 + num2;
        }
    }
}
