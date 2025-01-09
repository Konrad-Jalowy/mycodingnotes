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