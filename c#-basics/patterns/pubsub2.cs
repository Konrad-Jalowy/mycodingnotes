namespace ConsoleApp18
{
    using System;
    using System.Collections.Generic;

    class Publisher
    {
        private List<Action<string>> _subscribers = new List<Action<string>>();

        public void Subscribe(Action<string> subscriber)
        {
            _subscribers.Add(subscriber);
        }

        public void Unsubscribe(Action<string> subscriber)
        {
            _subscribers.Remove(subscriber);
        }

        public void Notify(string message)
        {
            foreach (var subscriber in _subscribers)
            {
                subscriber(message);
            }
        }
    }

    class Program
    {
        static void Main()
        {
            var publisher = new Publisher();

            // Subskrypcje
            Action<string> subscriber1 = (msg) => Console.WriteLine($"Subskrybent 1: {msg}");
            Action<string> subscriber2 = (msg) => Console.WriteLine($"Subskrybent 2: {msg}");

            publisher.Subscribe(subscriber1);
            publisher.Subscribe(subscriber2);

            // Powiadomienia
            publisher.Notify("Wiadomość testowa");

            publisher.Unsubscribe(subscriber1);

            publisher.Notify("Druga wiadomość");
        }
    }
}