using System;

namespace ConsoleApp20
{

    public class CustomEventArgs : EventArgs
    {
        public string Message { get; }
        public CustomEventArgs(string message)
        {
            Message = message;
        }
    }

    public class Publisher
    {
        public event EventHandler<CustomEventArgs> MyEvent;

        public void TriggerEvent(string message)
        {
            MyEvent?.Invoke(this, new CustomEventArgs(message));
        }
    }

    class Program
    {
        static void Main()
        {
            Publisher publisher = new Publisher();

            publisher.MyEvent += (sender, e) =>
            {
                Console.WriteLine($"Otrzymano zdarzenie: {e.Message}");
            };

            publisher.TriggerEvent("Cześć z EventArgs!");
        }
    }
}