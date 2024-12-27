namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string[] sArray = new string[] { "hi", "hello", "foo" };
            foreach(string msg in sArray)
            {
                Console.WriteLine(msg);
            }
        }
    }
}