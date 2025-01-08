namespace ConsoleApp18
{   
    class Game
    {
        private int MinRange { get; set; }
        private int MaxRange { get; set; }
        private int TargetNumber { get; set; }
        private int BestScore { get; set; } = int.MaxValue; 
        private int MaxAttempts { get; set; } 

        public Game()
        {
            MinRange = 1;
            MaxRange = 100;
        }

        public void StartGame()
        {
            Console.WriteLine("Witaj w grze 'Zgadywanie liczby'!");
            SetDifficulty();

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
            Console.WriteLine($"Komputer wylosował liczbę. Spróbuj zgadnąć! (Zakres: {MinRange} - {MaxRange}, Próby: {MaxAttempts})");

            int attempts = 0; 
            bool isCorrect = false;

            while (!isCorrect && attempts < MaxAttempts)
            {
                Console.Write("Podaj swoją liczbę: ");
                if (int.TryParse(Console.ReadLine(), out int guess))
                {
                    attempts++;

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
                        Console.WriteLine($"Gratulacje! Odgadłeś liczbę: {TargetNumber} w {attempts} próbach!");
                        isCorrect = true;

                        if (attempts < BestScore)
                        {
                            BestScore = attempts;
                            Console.WriteLine($"Nowy najlepszy wynik: {BestScore} próby!");
                        }
                        else
                        {
                            Console.WriteLine($"Najlepszy wynik to wciąż: {BestScore} próby.");
                        }
                    }
                }
                else
                {
                    Console.WriteLine("Nieprawidłowy format. Podaj liczbę całkowitą.");
                }
            }

            if (!isCorrect)
            {
                Console.WriteLine($"Przegrałeś! Wykorzystałeś wszystkie {MaxAttempts} próby. Liczba do odgadnięcia to: {TargetNumber}");
            }
        }

        private void GenerateRandomNumber()
        {
            Random random = new Random();
            TargetNumber = random.Next(MinRange, MaxRange + 1);
        }

        private void SetDifficulty()
        {
            Console.WriteLine("Wybierz poziom trudności:");
            Console.WriteLine("1. Łatwy (1 - 50, Próby: 10)");
            Console.WriteLine("2. Średni (1 - 100, Próby: 7)");
            Console.WriteLine("3. Trudny (1 - 200, Próby: 5)");
            Console.WriteLine("4. Własny zakres i próby");

            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    MinRange = 1;
                    MaxRange = 50;
                    MaxAttempts = 10;
                    break;
                case "2":
                    MinRange = 1;
                    MaxRange = 100;
                    MaxAttempts = 7;
                    break;
                case "3":
                    MinRange = 1;
                    MaxRange = 200;
                    MaxAttempts = 5;
                    break;
                case "4":
                    Console.Write("Podaj minimalny zakres: ");
                    MinRange = int.Parse(Console.ReadLine() ?? "1");

                    Console.Write("Podaj maksymalny zakres: ");
                    MaxRange = int.Parse(Console.ReadLine() ?? "100");

                    Console.Write("Podaj maksymalną liczbę prób: ");
                    MaxAttempts = int.Parse(Console.ReadLine() ?? "10");

                    if (MinRange >= MaxRange)
                    {
                        Console.WriteLine("Zakres nieprawidłowy. Ustawiam domyślny (1 - 100).");
                        MinRange = 1;
                        MaxRange = 100;
                    }
                    if (MaxAttempts <= 0)
                    {
                        Console.WriteLine("Liczba prób musi być większa od 0. Ustawiam domyślną wartość: 10.");
                        MaxAttempts = 10;
                    }
                    break;
                default:
                    Console.WriteLine("Nieprawidłowy wybór. Ustawiam domyślny poziom (1 - 100, Próby: 7).");
                    MinRange = 1;
                    MaxRange = 100;
                    MaxAttempts = 7;
                    break;
            }

            Console.WriteLine($"Zakres ustawiony na: {MinRange} - {MaxRange}, Maksymalna liczba prób: {MaxAttempts}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Game game = new Game();
            game.StartGame();
        }
    }
}
