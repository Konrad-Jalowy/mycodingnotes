namespace ConsoleApp18
{
    class Gracz
    {
        public delegate void PunktyZmienioneDelegate(int nowePunkty);
        public event PunktyZmienioneDelegate PunktyZmienione;

        private int _punkty;
        public int Punkty
        {
            get => _punkty;
            set
            {
                _punkty = value;
                PunktyZmienione?.Invoke(_punkty); // Powiadomienie o zmianie
            }
        }
    }

    class Program
    {
        static void Main()
        {
            var gracz = new Gracz();

            // Subskrybenci
            gracz.PunktyZmienione += WyświetlNaKonsoli;
            gracz.PunktyZmienione += ZapiszDoSystemu;

            // Zmiana punktów
            gracz.Punkty = 10;
            gracz.Punkty = 20;
        }

        static void WyświetlNaKonsoli(int nowePunkty)
        {
            Console.WriteLine($"Konsola: Gracz ma teraz {nowePunkty} punktów.");
        }

        static void ZapiszDoSystemu(int nowePunkty)
        {
            Console.WriteLine($"System: Zapisano punkty: {nowePunkty}");
        }
    }
}