namespace ConsoleApp18
{
    using System;

    public class Singleton
    {
        private static Singleton _instance;
        private static readonly object _lock = new object();

        private Singleton()
        {
            Console.WriteLine("Singleton instance created.");
        }

        public static Singleton Instance
        {
            get
            {
                lock (_lock)
                {
                    if (_instance == null)
                    {
                        _instance = new Singleton();
                    }
                }
                return _instance;
            }
        }

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
