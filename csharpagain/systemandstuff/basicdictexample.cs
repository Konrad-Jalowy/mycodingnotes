using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Tworzenie słownika
        Dictionary<string, int> ageDict = new Dictionary<string, int>();

        // Dodawanie elementów
        ageDict["Alice"] = 25; // Alternatywa dla Add
        ageDict.Add("Bob", 30);
        ageDict.Add("Charlie", 35);

        // Wyświetlanie słownika
        Console.WriteLine("Słownik:");
        foreach (var entry in ageDict)
        {
            Console.WriteLine($"Klucz: {entry.Key}, Wartość: {entry.Value}");
        }

        // Pobieranie wartości
        Console.WriteLine($"Wiek Alice: {ageDict["Alice"]}");

        // Sprawdzanie obecności klucza/wartości
        Console.WriteLine($"Czy istnieje klucz 'Bob'? {ageDict.ContainsKey("Bob")}");
        Console.WriteLine($"Czy istnieje wartość 30? {ageDict.ContainsValue(30)}");

        // Usuwanie elementu
        ageDict.Remove("Charlie");
        Console.WriteLine("Po usunięciu Charliego:");
        foreach (var entry in ageDict)
        {
            Console.WriteLine($"Klucz: {entry.Key}, Wartość: {entry.Value}");
        }

        // Sprawdzanie rozmiaru
        Console.WriteLine($"Rozmiar słownika: {ageDict.Count}");
    }
}
