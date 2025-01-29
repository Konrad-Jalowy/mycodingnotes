using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<string> words = new List<string> { "kot", "pies", "kot", "słoń", "pies", "kot" };

        var wordCount = words.GroupBy(w => w).ToDictionary(g => g.Key, g => g.Count());

        foreach (var kvp in wordCount)
        {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        }
    }
}
