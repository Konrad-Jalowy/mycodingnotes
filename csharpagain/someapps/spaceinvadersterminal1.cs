using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace SpaceInvadersTerminal
{
    class Program
    {
        static void Main(string[] args)
        {
            Game game = new Game();
            game.Start();
        }
    }

    // Reprezentuje pozycję na ekranie
    public struct Position
    {
        public int X;
        public int Y;

        public Position(int x, int y)
        {
            this.X = x;
            this.Y = y;
        }
    }

    // Klasa bazowa dla wszystkich obiektów w grze
    public abstract class GameObject
    {
        public Position Position;
        public char Symbol;

        public GameObject(int x, int y, char symbol)
        {
            Position = new Position(x, y);
            Symbol = symbol;
        }

        public abstract void Update(Game game);
    }

    // Statek gracza
    public class Player : GameObject
    {
        private int shootCooldown = 0;
        private const int CooldownTime = 15; // Zwiększony czas cooldownu

        public Player(int x, int y) : base(x, y, 'A') { }

        public override void Update(Game game)
        {
            if (shootCooldown > 0)
                shootCooldown--;
        }

        public void Shoot(Game game)
        {
            if (shootCooldown == 0)
            {
                // Dodanie nowego pocisku nad graczem
                lock (game.gameLock)
                {
                    // Zapobieganie wielokrotnemu strzelaniu z tego samego miejsca
                    if (!game.PlayerBullets.Any(b => b.Position.X == Position.X && b.Position.Y == Position.Y - 1))
                    {
                        game.PlayerBullets.Add(new Bullet(Position.X, Position.Y - 1, '^', true));
                        shootCooldown = CooldownTime;
                    }
                }
            }
        }
    }

    // Statek wroga
    public class Enemy : GameObject
    {
        private int deathTimer = 0;
        private static readonly object randLock = new object();
        private static readonly Random rand = new Random();

        public bool IsDead { get; private set; } = false;

        public Enemy(int x, int y, char symbol) : base(x, y, symbol) { }

        public override void Update(Game game)
        {
            if (IsDead)
            {
                deathTimer--;
                if (deathTimer <= 0)
                {
                    lock (game.gameLock)
                    {
                        game.EnemiesToRemove.Add(this);
                    }
                }
            }
            else
            {
                // Prosty mechanizm strzelania z niskim prawdopodobieństwem
                double shootProbability;
                lock (randLock)
                {
                    shootProbability = rand.NextDouble();
                }
                if (shootProbability < 0.001) // Zmniejszone prawdopodobieństwo
                {
                    lock (game.gameLock)
                    {
                        game.EnemyBullets.Add(new Bullet(Position.X, Position.Y + 1, 'v', false));
                    }
                }
            }
        }

        public void MarkAsDead()
        {
            if (!IsDead)
            {
                IsDead = true;
                deathTimer = 10; // Liczba klatek do wyświetlenia '#'
                Symbol = '#';
            }
        }
    }

    // Klasa pocisku
    public class Bullet : GameObject
    {
        public bool FromPlayer;

        public Bullet(int x, int y, char symbol, bool fromPlayer) : base(x, y, symbol)
        {
            FromPlayer = fromPlayer;
        }

        public override void Update(Game game)
        {
            // Ruch pocisku
            if (FromPlayer)
                Position = new Position(Position.X, Position.Y - 1);
            else
                Position = new Position(Position.X, Position.Y + 1);
        }
    }

    // Główna klasa gry
    public class Game
    {
        public int Width = 80;
        public int Height = 25;

        public Player Player;
        public List<Enemy> Enemies = new List<Enemy>();
        public List<Bullet> PlayerBullets = new List<Bullet>();
        public List<Bullet> EnemyBullets = new List<Bullet>();
        public List<Enemy> EnemiesToRemove = new List<Enemy>();

        public object gameLock = new object();

        private bool running = true;

        public Game()
        {
            try
            {
                Console.CursorVisible = false;
                // Ustawienie rozmiaru konsoli, zabezpieczając przed zbyt małym rozmiarem
                if (Console.LargestWindowWidth >= Width && Console.LargestWindowHeight >= Height)
                {
                    Console.SetWindowSize(Width, Height);
                    Console.SetBufferSize(Width, Height);
                }
                else
                {
                    Console.SetWindowSize(Math.Min(Width, Console.LargestWindowWidth), Math.Min(Height, Console.LargestWindowHeight));
                    Console.SetBufferSize(Math.Min(Width, Console.LargestWindowWidth), Math.Min(Height, Console.LargestWindowHeight));
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Nie można ustawić rozmiaru konsoli: " + ex.Message);
                // Kontynuuj z bieżącym rozmiarem konsoli
            }

            // Inicjalizacja gracza na dole środka ekranu
            Player = new Player(Width / 2, Height - 2);

            // Inicjalizacja wrogów w siatce
            int rows = 5;
            int cols = 10;
            int startX = 5;
            int startY = 2;
            for (int row = 0; row < rows; row++)
            {
                for (int col = 0; col < cols; col++)
                {
                    char enemySymbol = (row % 2 == 0) ? 'M' : 'W';
                    Enemies.Add(new Enemy(startX + col * 6, startY + row * 2, enemySymbol));
                }
            }
        }

        public void Start()
        {
            // Rozpoczęcie wątku obsługującego wejście
            Thread inputThread = new Thread(InputHandler);
            inputThread.Start();

            // Rozpoczęcie głównej pętli gry
            GameLoop();

            // Oczekiwanie na zakończenie wątku wejścia
            inputThread.Join();
        }

        private void InputHandler()
        {
            while (running)
            {
                if (Console.KeyAvailable)
                {
                    var keyInfo = Console.ReadKey(true);
                    lock (gameLock)
                    {
                        switch (keyInfo.Key)
                        {
                            case ConsoleKey.LeftArrow:
                                if (Player.Position.X > 0)
                                    Player.Position = new Position(Player.Position.X - 1, Player.Position.Y);
                                break;
                            case ConsoleKey.RightArrow:
                                if (Player.Position.X < Width - 1)
                                    Player.Position = new Position(Player.Position.X + 1, Player.Position.Y);
                                break;
                            case ConsoleKey.Spacebar:
                                Player.Shoot(this);
                                break;
                            case ConsoleKey.Escape:
                                running = false;
                                break;
                        }
                    }
                }
                Thread.Sleep(1); // Krótkie opóźnienie, aby nie obciążać CPU
            }
        }

        private void GameLoop()
        {
            DateTime lastTime = DateTime.Now;
            double delta = 0;

            while (running)
            {
                DateTime now = DateTime.Now;
                delta += (now - lastTime).TotalMilliseconds;
                lastTime = now;

                while (delta >= 16.67) // Około 60 FPS
                {
                    UpdateGame();
                    delta -= 16.67;
                }

                Render();

                Thread.Sleep(1); // Krótkie opóźnienie, aby nie obciążać CPU
            }

            // Ekran końcowy gry
            Console.Clear();
            string message;
            if (Enemies.Count == 0)
                message = "You Win!";
            else
                message = "Game Over!";

            // Obliczenie pozycji do wyśrodkowania komunikatu
            int msgX = Math.Max((Width / 2) - (message.Length / 2), 0);
            int msgY = Height / 2;

            try
            {
                Console.SetCursorPosition(msgX, msgY);
                Console.Write(message);
                Console.SetCursorPosition(0, msgY + 1);
                Console.Write("Press any key to exit...");
                Console.ReadKey(true); // Oczekiwanie na naciśnięcie klawisza
            }
            catch (ArgumentOutOfRangeException)
            {
                // Jeśli konsola jest za mała
                Console.WriteLine(message);
                Console.WriteLine("Press any key to exit...");
                Console.ReadKey(true);
            }
        }

        private void UpdateGame()
        {
            lock (gameLock)
            {
                // Aktualizacja gracza
                Player.Update(this);

                // Aktualizacja wrogów
                foreach (var enemy in Enemies.ToList()) // ToList() aby uniknąć modyfikacji listy podczas iteracji
                {
                    enemy.Update(this);
                }

                // Aktualizacja pocisków gracza
                foreach (var bullet in PlayerBullets.ToList())
                {
                    bullet.Update(this);
                    if (bullet.Position.Y < 0)
                        PlayerBullets.Remove(bullet);
                    else
                    {
                        // Sprawdzenie kolizji z wrogiem
                        var hitEnemy = Enemies.FirstOrDefault(e => !e.IsDead && e.Position.X == bullet.Position.X && e.Position.Y == bullet.Position.Y);
                        if (hitEnemy != null)
                        {
                            hitEnemy.MarkAsDead();
                            PlayerBullets.Remove(bullet);
                        }
                    }
                }

                // Aktualizacja pocisków wrogów
                foreach (var bullet in EnemyBullets.ToList())
                {
                    bullet.Update(this);
                    if (bullet.Position.Y >= Height)
                        EnemyBullets.Remove(bullet);
                    else
                    {
                        // Sprawdzenie kolizji z graczem
                        if (bullet.Position.X == Player.Position.X && bullet.Position.Y == Player.Position.Y)
                        {
                            running = false;
                        }
                    }
                }

                // Usuwanie zniszczonych wrogów
                foreach (var enemy in EnemiesToRemove.ToList())
                {
                    Enemies.Remove(enemy);
                }
                EnemiesToRemove.Clear();

                // Sprawdzenie warunku wygranej
                bool anyAlive = Enemies.Any(e => !e.IsDead);
                if (!anyAlive)
                {
                    running = false;
                }
            }
        }

        private void Render()
        {
            StringBuilder buffer = new StringBuilder(new string(' ', Width * Height));

            lock (gameLock)
            {
                // Rysowanie wrogów
                foreach (var enemy in Enemies)
                {
                    SetChar(buffer, enemy.Position.X, enemy.Position.Y, enemy.Symbol);
                }

                // Rysowanie pocisków gracza
                foreach (var bullet in PlayerBullets)
                {
                    if (bullet.Position.Y >= 0 && bullet.Position.Y < Height)
                        SetChar(buffer, bullet.Position.X, bullet.Position.Y, bullet.Symbol);
                }

                // Rysowanie pocisków wrogów
                foreach (var bullet in EnemyBullets)
                {
                    if (bullet.Position.Y >= 0 && bullet.Position.Y < Height)
                        SetChar(buffer, bullet.Position.X, bullet.Position.Y, bullet.Symbol);
                }

                // Rysowanie gracza
                SetChar(buffer, Player.Position.X, Player.Position.Y, Player.Symbol);
            }

            // Renderowanie bufora na konsolę
            try
            {
                Console.SetCursorPosition(0, 0);
                for (int y = 0; y < Height; y++)
                {
                    int start = y * Width;
                    string line = buffer.ToString(start, Width);
                    Console.Write(line);
                }
            }
            catch (ArgumentOutOfRangeException)
            {
                // Jeśli konsola jest za mała, nie robić nic
            }
        }

        private void SetChar(StringBuilder buffer, int x, int y, char c)
        {
            if (x >= 0 && x < Width && y >= 0 && y < Height)
                buffer[y * Width + x] = c;
        }
    }
}
