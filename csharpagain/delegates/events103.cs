namespace ConsoleApp20
{
    using System;

    namespace ConsoleApp
    {
        // Argumenty zdarzenia
        public class CustomEventArgs : EventArgs
        {
            public string Message { get; }

            public CustomEventArgs(string message)
            {
                Message = message;
            }
        }

        // Klasa Publisher
        public class Publisher
        {
            // Deklaracja zdarzenia
            public event EventHandler<CustomEventArgs> MyEvent;

            // Wywołanie zdarzenia
            public void TriggerEvent(string message)
            {
                Console.WriteLine("Publisher: Wywoływanie zdarzenia...");
                MyEvent?.Invoke(this, new CustomEventArgs(message));
            }
        }

        // Klasa Subscriber
        public class Subscriber
        {
            private readonly string _name;

            public Subscriber(string name)
            {
                _name = name;
            }

            // Metoda obsługi zdarzenia
            public void HandleEvent(object sender, CustomEventArgs e)
            {
                Console.WriteLine($"Subscriber {_name}: Otrzymano wiadomość: {e.Message}");
                Console.WriteLine($"Subscriber {_name}: Zdarzenie wysłane przez: {sender}");
            }
        }

        class Program
        {
            static void Main(string[] args)
            {
                // Tworzenie Publishera
                Publisher publisher = new Publisher();

                // Tworzenie dwóch Subskrybentów
                Subscriber sub1 = new Subscriber("A");
                Subscriber sub2 = new Subscriber("B");

                // Subskrybowanie zdarzenia przez subskrybentów
                publisher.MyEvent += sub1.HandleEvent;
                publisher.MyEvent += sub2.HandleEvent;

                // Wywołanie zdarzenia
                publisher.TriggerEvent("Cześć, subskrybenci!");

                // Odsubskrybowanie pierwszego subskrybenta
                publisher.MyEvent -= sub1.HandleEvent;

                // Wywołanie zdarzenia po odsubskrybowaniu
                publisher.TriggerEvent("Cześć, tylko subskrybent B!");
            }
        }
    }

}