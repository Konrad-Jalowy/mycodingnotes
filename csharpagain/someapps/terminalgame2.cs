using System.Threading;

namespace TerminalGame
{
    class Program
    {
        static void Main(string[] args)
        {
            int width = 20; // Szerokość planszy
            int height = 10; // Wysokość planszy
            int playerX = 0; // Pozycja X gracza
            int playerY = 0; // Pozycja Y gracza

            // Losowa pozycja celu
            Random random = new Random();
            int targetX = random.Next(width);
            int targetY = random.Next(height);

            // Przeciwnicy
            int enemyCount = 3;
            int[,] enemies = new int[enemyCount, 2];
            for (int i = 0; i < enemyCount; i++)
            {
                enemies[i, 0] = random.Next(width); // X przeciwnika
                enemies[i, 1] = random.Next(height); // Y przeciwnika
            }

            ConsoleKey key;
            bool gameRunning = true;

            // Wątek do poruszania przeciwników
            Thread enemyThread = new Thread(() => MoveEnemies(enemies, width, height, () => gameRunning));
            enemyThread.Start();

            do
            {
                Console.Clear();

                // Rysowanie planszy
                for (int y = 0; y < height; y++)
                {
                    for (int x = 0; x < width; x++)
                    {
                        if (x == playerX && y == playerY)
                        {
                            Console.Write("@"); // Gracz
                        }
                        else if (x == targetX && y == targetY)
                        {
                            Console.Write("X"); // Cel
                        }
                        else if (IsEnemyAtPosition(enemies, x, y))
                        {
                            Console.Write("E"); // Przeciwnik
                        }
                        else
                        {
                            Console.Write("."); // Puste pole
                        }
                    }
                    Console.WriteLine();
                }

                // Sprawdzenie, czy gracz dotarł do celu
                if (playerX == targetX && playerY == targetY)
                {
                    Console.WriteLine("Congratulations! You reached the goal!");
                    gameRunning = false;
                    break;
                }

                // Sprawdzenie kolizji z przeciwnikiem
                if (IsEnemyAtPosition(enemies, playerX, playerY))
                {
                    Console.WriteLine("Game Over! You were caught by an enemy.");
                    gameRunning = false;
                    break;
                }

                // Sterowanie gracza
                key = Console.ReadKey(true).Key;
                switch (key)
                {
                    case ConsoleKey.W: // Góra
                        if (playerY > 0) playerY--;
                        break;
                    case ConsoleKey.A: // Lewo
                        if (playerX > 0) playerX--;
                        break;
                    case ConsoleKey.S: // Dół
                        if (playerY < height - 1) playerY++;
                        break;
                    case ConsoleKey.D: // Prawo
                        if (playerX < width - 1) playerX++;
                        break;
                }

            } while (key != ConsoleKey.Escape && gameRunning); // Wyjście klawiszem Esc lub zakończenie gry

            gameRunning = false; // Zatrzymanie wątku przeciwników
            enemyThread.Join(); // Poczekaj na zakończenie wątku

            Console.WriteLine("Game over! Press any key to exit...");
            Console.ReadKey();
        }

        private static void MoveEnemies(int[,] enemies, int width, int height, Func<bool> isGameRunning)
        {
            Random random = new Random();

            while (isGameRunning())
            {
                for (int i = 0; i < enemies.GetLength(0); i++)
                {
                    // Losowy ruch przeciwnika
                    int direction = random.Next(4);
                    switch (direction)
                    {
                        case 0: // Góra
                            if (enemies[i, 1] > 0) enemies[i, 1]--;
                            break;
                        case 1: // Dół
                            if (enemies[i, 1] < height - 1) enemies[i, 1]++;
                            break;
                        case 2: // Lewo
                            if (enemies[i, 0] > 0) enemies[i, 0]--;
                            break;
                        case 3: // Prawo
                            if (enemies[i, 0] < width - 1) enemies[i, 0]++;
                            break;
                    }
                }

                Thread.Sleep(500); // Czas między ruchami przeciwników
            }
        }

        private static bool IsEnemyAtPosition(int[,] enemies, int x, int y)
        {
            for (int i = 0; i < enemies.GetLength(0); i++)
            {
                if (enemies[i, 0] == x && enemies[i, 1] == y)
                {
                    return true;
                }
            }
            return false;
        }
    }
}
