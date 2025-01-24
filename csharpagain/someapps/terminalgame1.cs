namespace TextEditorApp
{
    using System;

    namespace TerminalGame
    {
        class Program
        {
            static void Main(string[] args)
            {
                int width = 10; // Szerokość planszy
                int height = 10; // Wysokość planszy
                int playerX = 0; // Pozycja X gracza
                int playerY = 0; // Pozycja Y gracza

                // Losowa pozycja celu
                Random random = new Random();
                int targetX = random.Next(width);
                int targetY = random.Next(height);

                ConsoleKey key;
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
                        break;
                    }

                    // Sterowanie
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

                } while (key != ConsoleKey.Escape); // Wyjście klawiszem Esc
            }
        }
    }

}
