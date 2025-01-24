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
                enemies[i, 0] = random.Next(width);
                enemies[i, 1] = random.Next(height);
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
                        Console.WriteLine("Congratulations! You reached the goal!");
                        MarkFinalState("*", "X"); // Rysuj gracza na celu
                    }

                    // Sprawdzenie kolizji z przeciwnikiem
                    if (IsEnemyAtPosition(playerX, playerY))
                    {
                        gameRunning = false;
                        Console.SetCursorPosition(0, height + 1);
                        Console.WriteLine("Game Over! You were caught by an enemy.");
                        MarkFinalState("X", "E"); // Rysuj gracza na przeciwniku
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
                                    Console.Write("*"); // Gracz na celu
                                else if (IsEnemyAtPosition(x, y))
                                    Console.Write("X"); // Gracz na przeciwniku
                                else
                                    Console.Write("@"); // Gracz
                            }
                            else if (x == targetX && y == targetY)
                                Console.Write("X"); // Cel
                            else if (IsEnemyAtPosition(x, y))
                                Console.Write("E"); // Przeciwnik
                            else
                                Console.Write(".");
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
                        switch (direction)
                        {
                            case 0: if (enemies[i, 1] > 0) enemies[i, 1]--; break; // Góra
                            case 1: if (enemies[i, 1] < height - 1) enemies[i, 1]++; break; // Dół
                            case 2: if (enemies[i, 0] > 0) enemies[i, 0]--; break; // Lewo
                            case 3: if (enemies[i, 0] < width - 1) enemies[i, 0]++; break; // Prawo
                        }
                    }
                }

                Thread.Sleep(500); // Ruch przeciwników co 500 ms
            }
        }

        private static void MarkFinalState(string playerSymbol, string collisionSymbol)
        {
            lock (lockObject)
            {
                Console.SetCursorPosition(0, 0);

                for (int y = 0; y < height; y++)
                {
                    for (int x = 0; x < width; x++)
                    {
                        if (x == playerX && y == playerY)
                            Console.Write(collisionSymbol); // Kolizja
                        else if (x == targetX && y == targetY)
                            Console.Write("X"); // Cel
                        else if (IsEnemyAtPosition(x, y))
                            Console.Write("E");
                        else
                            Console.Write(".");
                    }
                    Console.WriteLine();
                }
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
