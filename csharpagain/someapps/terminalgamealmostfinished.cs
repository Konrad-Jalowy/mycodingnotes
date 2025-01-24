using System.Threading;


namespace TerminalGame
{
    class Program
    {
        private static readonly object lockObject = new object();
        private static int width = 20;
        private static int height = 10;
        private static int playerX = 0;
        private static int playerY = 0;
        private static int[,] enemies;
        private static int enemyCount = 3;
        private static int targetX;
        private static int targetY;
        private static bool gameRunning = true;

        static void Main(string[] args)
        {
            Console.CursorVisible = false; // Ukryj kursor na czas gry

            Random random = new Random();
            targetX = random.Next(width);
            targetY = random.Next(height);

            // Inicjalizacja przeciwników
            enemies = new int[enemyCount, 2];
            for (int i = 0; i < enemyCount; i++)
            {
                do
                {
                    enemies[i, 0] = random.Next(width);
                    enemies[i, 1] = random.Next(height);
                } while (enemies[i, 0] == targetX && enemies[i, 1] == targetY); // Unikaj celu
            }

            // Wątki do odświeżania ekranu i ruchu przeciwników
            Thread enemyThread = new Thread(MoveEnemies);
            Thread renderThread = new Thread(RenderGame);

            enemyThread.Start();
            renderThread.Start();

            // Sterowanie graczem
            while (gameRunning)
            {
                ConsoleKey key = Console.ReadKey(true).Key; // Nie pokazuj naciśniętego klawisza
                lock (lockObject)
                {
                    switch (key)
                    {
                        case ConsoleKey.W: if (playerY > 0) playerY--; break;
                        case ConsoleKey.A: if (playerX > 0) playerX--; break;
                        case ConsoleKey.S: if (playerY < height - 1) playerY++; break;
                        case ConsoleKey.D: if (playerX < width - 1) playerX++; break;
                        case ConsoleKey.Escape: gameRunning = false; break;
                    }

                    // Sprawdzenie wygranej
                    if (playerX == targetX && playerY == targetY)
                    {
                        gameRunning = false;
                        Console.SetCursorPosition(0, height + 1);
                        Console.ForegroundColor = ConsoleColor.Green; // Zielony dla wygranej
                        Console.WriteLine("Congratulations! You reached the goal!");
                        Console.ResetColor();
                        MarkFinalState(); // Rysuj końcowy stan gry
                    }

                    // Sprawdzenie kolizji z przeciwnikiem
                    if (IsEnemyAtPosition(playerX, playerY))
                    {
                        gameRunning = false;
                        Console.SetCursorPosition(0, height + 1);
                        Console.ForegroundColor = ConsoleColor.Red; // Czerwony dla przegranej
                        Console.WriteLine("Game Over! You were caught by an enemy.");
                        Console.ResetColor();
                        MarkFinalState(); // Rysuj końcowy stan gry
                    }

                    if (!gameRunning)
                    {
                        Monitor.PulseAll(lockObject); // Obudź wszystkie wątki
                    }
                }
            }

            lock (lockObject)
            {
                Monitor.PulseAll(lockObject); // Upewnij się, że wszystkie wątki się zakończą
            }

            enemyThread.Join();
            renderThread.Join();

            Console.CursorVisible = true; // Przywróć widoczność kursora po zakończeniu gry
            Console.SetCursorPosition(0, height + 2);
            Console.WriteLine("Game over! Press any key to exit...");
            Console.ReadKey(true); // Nie pokazuj naciśniętego klawisza
        }

        private static void RenderGame()
        {
            while (true)
            {
                lock (lockObject)
                {
                    if (!gameRunning)
                        break;

                    Console.SetCursorPosition(0, 0); // Resetuj kursor zamiast czyszczenia konsoli
                    for (int y = 0; y < height; y++)
                    {
                        for (int x = 0; x < width; x++)
                        {
                            if (x == playerX && y == playerY)
                            {
                                if (x == targetX && y == targetY)
                                    Console.ForegroundColor = ConsoleColor.Cyan; // Gracz na celu
                                else if (IsEnemyAtPosition(x, y))
                                    Console.ForegroundColor = ConsoleColor.Yellow; // Gracz na przeciwniku
                                else
                                    Console.ForegroundColor = ConsoleColor.Green; // Gracz
                                Console.Write("@");
                            }
                            else if (x == targetX && y == targetY)
                            {
                                Console.ForegroundColor = ConsoleColor.Blue; // Cel
                                Console.Write("X");
                            }
                            else if (IsEnemyAtPosition(x, y))
                            {
                                Console.ForegroundColor = ConsoleColor.Red; // Przeciwnik
                                Console.Write("E");
                            }
                            else
                            {
                                Console.ResetColor(); // Tło
                                Console.Write(".");
                            }
                        }
                        Console.WriteLine();
                    }
                }

                Thread.Sleep(10); // 100 FPS
            }
        }

        private static void MoveEnemies()
        {
            Random random = new Random();

            while (true)
            {
                lock (lockObject)
                {
                    if (!gameRunning)
                        break;

                    for (int i = 0; i < enemyCount; i++)
                    {
                        int direction = random.Next(4);
                        int newX = enemies[i, 0];
                        int newY = enemies[i, 1];

                        switch (direction)
                        {
                            case 0: if (newY > 0) newY--; break; // Góra
                            case 1: if (newY < height - 1) newY++; break; // Dół
                            case 2: if (newX > 0) newX--; break; // Lewo
                            case 3: if (newX < width - 1) newX++; break; // Prawo
                        }

                        // Unikaj celu
                        if (newX != targetX || newY != targetY)
                        {
                            enemies[i, 0] = newX;
                            enemies[i, 1] = newY;
                        }
                    }
                }

                Thread.Sleep(500); // Ruch przeciwników co 500 ms
            }
        }

        private static void MarkFinalState()
        {
            lock (lockObject)
            {
                Console.SetCursorPosition(0, 0);

                for (int y = 0; y < height; y++)
                {
                    for (int x = 0; x < width; x++)
                    {
                        if (x == playerX && y == playerY && x == targetX && y == targetY)
                        {
                            Console.ForegroundColor = ConsoleColor.Cyan; // Gracz na celu
                            Console.Write("*");
                        }
                        else if (x == playerX && y == playerY && IsEnemyAtPosition(x, y))
                        {
                            Console.ForegroundColor = ConsoleColor.Yellow; // Gracz na przeciwniku
                            Console.Write("#");
                        }
                        else if (x == playerX && y == playerY)
                        {
                            Console.ForegroundColor = ConsoleColor.Green; // Gracz
                            Console.Write("@");
                        }
                        else if (x == targetX && y == targetY)
                        {
                            Console.ForegroundColor = ConsoleColor.Blue; // Cel
                            Console.Write("X");
                        }
                        else if (IsEnemyAtPosition(x, y))
                        {
                            Console.ForegroundColor = ConsoleColor.Red; // Przeciwnik
                            Console.Write("E");
                        }
                        else
                        {
                            Console.ResetColor(); // Tło
                            Console.Write(".");
                        }
                    }
                    Console.WriteLine();
                }
                Console.ResetColor(); // Przywróć domyślny kolor po zakończeniu
            }
        }

        private static bool IsEnemyAtPosition(int x, int y)
        {
            for (int i = 0; i < enemyCount; i++)
            {
                if (enemies[i, 0] == x && enemies[i, 1] == y)
                    return true;
            }
            return false;
        }
    }
}
