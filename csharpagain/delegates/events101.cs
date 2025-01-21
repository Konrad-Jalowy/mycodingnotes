using System;

namespace ConsoleApp20
{
    class Button
    {
        public event Action Clicked; // Zdarzenie

        public void Click()
        {
            Console.WriteLine("Button clicked!");
            Clicked?.Invoke(); // Wywołanie zdarzenia, jeśli są subskrybenci
        }
    }

    class Program
    {
        static void Main()
        {
            Button button = new Button();
            button.Clicked += () => Console.WriteLine("Button has been clicked!"); // Subskrypcja
            button.Click();
        }
    }
}