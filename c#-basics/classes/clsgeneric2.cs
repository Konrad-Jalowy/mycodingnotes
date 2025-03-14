namespace ConsoleApp15
{
    class GenericObj<T> where T: struct
    {
        public T Data { get; set; }

        public GenericObj(T data)
        {
            Data = data;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hi!");

            /*GenericObj<string> obj1 = new GenericObj<string>("Hello World");*/
            GenericObj<int> obj2 = new GenericObj<int>(123);
            GenericObj<bool> obj3 = new GenericObj<bool>(true);
            /*GenericObj<Thread> obj4 = new GenericObj<Thread>(new Thread(() => {
                Thread.Sleep(1000);
                Console.WriteLine("Hello world");
            }));*/

            /*Console.WriteLine(obj1.Data);*/
            Console.WriteLine(obj2.Data);
            Console.WriteLine(obj3.Data);
        }
    }
}