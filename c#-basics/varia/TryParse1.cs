namespace ConsoleApp13
{
    class Program
    {
        static void Main(string[] args)
        {
            string okString = "1";
            string wrongString = "one";

            bool ok1 = int.TryParse(okString, out int parsed1);

            if (ok1)
            {
                Console.WriteLine(parsed1);
            }

            bool ok2 = int.TryParse(wrongString, out int parsed2);

            if (!ok2)
            {
                Console.WriteLine("Something went wrong");
            }
        }
    }
}
