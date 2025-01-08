namespace ConsoleApp18
{
    public class Singleton
    {

        private static Singleton _instance;

        private Singleton()
        {
            Console.WriteLine("Singleton instance created.");
        }
        
        public static Singleton Instance
        {
            get
            {
                if (_instance == null)
                {
                    _instance = new Singleton();
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
            
            Singleton s1 = Singleton.Instance;
            s1.DoSomething();
           
            Singleton s2 = Singleton.Instance;
           
            if (s1 == s2)
            {
                Console.WriteLine("Both instances are the same!");
            }
        }
    }
}
