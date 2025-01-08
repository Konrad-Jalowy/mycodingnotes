namespace ConsoleApp18
{
    class Game
    {
        private int MinRange { get; set; }
        private int MaxRange { get; set; }
        private int TargetNumber { get; set; }

        public Game(int minRange, int maxRange)
        {
            MinRange = minRange;
            MaxRange = maxRange;
        }

        public void StartGame()
        {
            Console.WriteLine($"Witaj w grze 'Zgadywanie liczby'! Zakres: {MinRange} - {MaxRange}");

            bool playAgain = true;
            while (playAgain)
            {
                PlayRound();
                Console.Write("Czy chcesz zagrać ponownie? (tak/nie): ");
                string response = Console.ReadLine()?.ToLower();
                playAgain = response == "tak";
            }

            Console.WriteLine("Dziękujemy za grę! Do zobaczenia!");
        }

        private void PlayRound()
        {
            GenerateRandomNumber();
            Console.WriteLine($"Komputer wylosował liczbę. Spróbuj zgadnąć!");

            bool isCorrect = false;
            while (!isCorrect)
            {
                Console.Write("Podaj swoją liczbę: ");
                if (int.TryParse(Console.ReadLine(), out int guess))
                {
                    if (guess < TargetNumber)
                    {
                        Console.WriteLine("Za mało! Spróbuj jeszcze raz.");
                    }
                    else if (guess > TargetNumber)
                    {
                        Console.WriteLine("Za dużo! Spróbuj jeszcze raz.");
                    }
                    else
                    {
                        Console.WriteLine($"Gratulacje! Odgadłeś liczbę: {TargetNumber}");
                        isCorrect = true;
                    }
                }
                else
                {
                    Console.WriteLine("Nieprawidłowy format. Podaj liczbę całkowitą.");
                }
            }
        }

        private void GenerateRandomNumber()
        {
            Random random = new Random();
            TargetNumber = random.Next(MinRange, MaxRange + 1);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            
            Game game = new Game(1, 100);
            game.StartGame();
        }
    }
}
