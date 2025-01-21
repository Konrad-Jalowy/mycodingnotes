using System;

namespace ConsoleApp20
{
    public class Publisher
    {
        // Deklaracja zdarzenia
        public event Action<string> MyEvent;

        // Wywołanie zdarzenia
        public void TriggerEvent(string message)
        {
            Console.WriteLine("Wywoływanie zdarzenia...");
            MyEvent?.Invoke(message); // Wywołanie zdarzenia (jeśli są subskrybenci)
        }
    }

    public class Subscriber
    {
        private readonly string _name;

        public Subscriber(string name)
        {
            _name = name;
        }

        public void OnEventOccur(string message)
        {
            Console.WriteLine($"Subskrybent {_name} otrzymał wiadomość: {message}");
        }
    }

    class Program
    {
        static void Main()
        {
            Publisher publisher = new Publisher();

            // Tworzenie subskrybentów
            Subscriber sub1 = new Subscriber("A");
            Subscriber sub2 = new Subscriber("B");

            // Subskrybowanie zdarzeń
            publisher.MyEvent += sub1.OnEventOccur;
            publisher.MyEvent += sub2.OnEventOccur;

            // Wywołanie zdarzenia
            publisher.TriggerEvent("Cześć wszystkim!");

            // Odsubskrybowanie
            publisher.MyEvent -= sub1.OnEventOccur;
            publisher.TriggerEvent("Tylko subskrybent B!");
        }
    }
}