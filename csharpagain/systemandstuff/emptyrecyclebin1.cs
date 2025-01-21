 using System;
    using System.Runtime.InteropServices;

    class Program
    {
        // Import funkcji SHEmptyRecycleBin z shell32.dll
        [DllImport("shell32.dll", CharSet = CharSet.Unicode)]
        private static extern int SHEmptyRecycleBin(IntPtr hwnd, string pszRootPath, int dwFlags);

        // Flagi dla funkcji SHEmptyRecycleBin
        private const int SHERB_NOCONFIRMATION = 0x00000001; // Brak potwierdzenia
        private const int SHERB_NOPROGRESSUI = 0x00000002;   // Brak okna postępu
        private const int SHERB_NOSOUND = 0x00000004;        // Brak dźwięku po zakończeniu

        static void Main(string[] args)
        {
            Console.WriteLine("Czy na pewno chcesz wyczyścić kosz? (t/n)");
            string input = Console.ReadLine()?.ToLower();

            if (input == "t")
            {
                // Próba opróżnienia kosza
                int result = SHEmptyRecycleBin(IntPtr.Zero, null, SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND);

                if (result == 0)
                {
                    Console.WriteLine("Kosz został pomyślnie wyczyszczony.");
                }
                else
                {
                    Console.WriteLine($"Wystąpił błąd podczas czyszczenia kosza. Kod błędu: {result}");
                }
            }
            else
            {
                Console.WriteLine("Anulowano czyszczenie kosza.");
            }
        }
    }

