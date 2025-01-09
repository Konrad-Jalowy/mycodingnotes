namespace ConsoleApp18
{
    using System;
    using System.Collections;

    class MyCollection : IEnumerable
    {
        private int[] data = { 1, 2, 3, 4, 5 };

        public IEnumerator GetEnumerator()
        {
            for (int i = 0; i < data.Length; i++)
            {
                yield return data[i];
            }
        }
    }

    class Program
    {
        static void Main()
        {
            var collection = new MyCollection();

            foreach (var item in collection)
            {
                Console.WriteLine(item); // Wyjście: 1, 2, 3, 4, 5
            }
        }
    }
}