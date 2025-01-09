namespace ConsoleApp18
{
    public delegate void Powiadomienie(string message);

    class Emitent
    {
        // Deklaracja eventu
        public event Powiadomienie NaZdarzenie;

        public void WywolajZdarzenie(string wiadomosc)
        {
            if (NaZdarzenie != null)
            {
                NaZdarzenie(wiadomosc); // Powiadomienie subskrybentów
            }
        }
    }
    class Program
    {
        static void Main()
        {
            var emitent = new Emitent();

            // Subskrybowanie zdarzeń
            emitent.NaZdarzenie += WyswietlNaKonsoli;
            emitent.NaZdarzenie += WyslijDoSystemu;

            // Wywołanie zdarzenia
            emitent.WywolajZdarzenie("Wiadomość testowa");
        }

        static void WyswietlNaKonsoli(string message)
        {
            Console.WriteLine($"Konsola: {message}");
        }

        static void WyslijDoSystemu(string message)
        {
            Console.WriteLine($"System: {message}");
        }
    }
}