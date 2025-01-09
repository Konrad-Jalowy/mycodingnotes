namespace ConsoleApp18
{
    public delegate void Akcja(string komunikat);

    class Program
    {
        static void PierwszaMetoda(string komunikat)
        {
            Console.WriteLine($"Pierwsza metoda: {komunikat}");
        }

        static void DrugaMetoda(string komunikat)
        {
            Console.WriteLine($"Druga metoda: {komunikat}");
        }

        static void Main()
        {
            Akcja akcja = PierwszaMetoda;  // Przypisujemy pierwszą metodę
            akcja += DrugaMetoda;          // Dodajemy drugą metodę

            akcja("Cześć!");  // Wywołujemy wszystkie przypisane metody

            akcja -= PierwszaMetoda;  // Usuwamy pierwszą metodę
            akcja("Tylko druga metoda działa.");  // Wywołujemy ponownie delegat
        }
    }
}