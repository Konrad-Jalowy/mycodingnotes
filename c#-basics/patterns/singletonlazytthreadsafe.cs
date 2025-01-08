namespace ConsoleApp18
{
    using System;

    public class Singleton
    {
        
        private static readonly Lazy<Singleton> _instance = new Lazy<Singleton>(() => new Singleton());
        private Singleton()
        {
            Console.WriteLine("Singleton instance created.");
        }

        public static Singleton Instance => _instance.Value;

        public void DoSomething()
        {
            Console.WriteLine("Singleton is doing something!");
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            
            Parallel.For(0, 10, i =>
            {
                Singleton s = Singleton.Instance;
                s.DoSomething();
            });
        }
    }
}
