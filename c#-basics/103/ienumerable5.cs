using System;
using System.Collections.Generic;
using System.Threading.Tasks;

class Program
{
    static async IAsyncEnumerable<int> GetDataAsync()
    {
        for (int i = 1; i <= 5; i++)
        {
            await Task.Delay(500); // Symulacja opóźnienia (np. zapytanie do bazy danych)
            yield return i;
        }
    }

    static async Task Main()
    {
        await foreach (var item in GetDataAsync())
        {
            Console.WriteLine(item); // Wyjście: 1, 2, 3, 4, 5 (z opóźnieniem)
        }
    }
}
