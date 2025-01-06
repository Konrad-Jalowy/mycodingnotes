namespace ConsoleApp18
{
    class Program
    {
        public static void write(object o)
        {
            int i = 1000;
            while (i-- > 0)
            {
                Console.Write(o);
            }
        }
        static void Main(string[] args)
        {
            
            Task.Factory.StartNew(write, "hello");

            Task t = new(write, "hi");
            t.Start();
        
        }
    }
}
