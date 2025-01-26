using System;
using System.Threading;

class SharedResource
{
    private bool isAvailable = false;
    private readonly object lockObject = new object();

    public void Produce()
    {
        lock (lockObject)
        {
            isAvailable = true;
            Console.WriteLine("Producent: dane gotowe.");
            Monitor.Pulse(lockObject); // Powiadomienie konsumenta
        }
    }

    public void Consume()
    {
        lock (lockObject)
        {
            while (!isAvailable)
            {
                Monitor.Wait(lockObject); // Konsument czeka na dane
            }
            Console.WriteLine("Konsument: dane odebrane.");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        SharedResource resource = new SharedResource();

        Thread producer = new Thread(resource.Produce);
        Thread consumer = new Thread(resource.Consume);

        consumer.Start();
        producer.Start();
    }
}
