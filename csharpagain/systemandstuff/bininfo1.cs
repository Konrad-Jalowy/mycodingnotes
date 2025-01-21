
    using System;
    using System.Runtime.InteropServices;
    class Program
    {
        [StructLayout(LayoutKind.Sequential)]
        public struct SHQUERYRBINFO
        {
            public int cbSize;
            public long i64Size;  // Całkowity rozmiar elementów w koszu w bajtach
            public long i64NumItems; // Liczba elementów w koszu
        }

        // Import funkcji SHQueryRecycleBin z shell32.dll
        [DllImport("shell32.dll", CharSet = CharSet.Unicode)]
        public static extern int SHQueryRecycleBin(string pszRootPath, ref SHQUERYRBINFO pSHQueryRBInfo);

        static void Main(string[] args)
        {
            SHQUERYRBINFO rbInfo = new SHQUERYRBINFO
            {
                cbSize = Marshal.SizeOf(typeof(SHQUERYRBINFO))
            };

            // Wywołanie funkcji SHQueryRecycleBin
            int result = SHQueryRecycleBin(null, ref rbInfo);

            if (result == 0) // 0 oznacza sukces
            {
                Console.WriteLine("Stan kosza systemowego:");
                Console.WriteLine($"Liczba elementów w koszu: {rbInfo.i64NumItems}");
                Console.WriteLine($"Rozmiar elementów w koszu: {rbInfo.i64Size / 1024.0 / 1024.0:F2} MB");
            }
            else
            {
                Console.WriteLine($"Nie udało się pobrać informacji o koszu. Kod błędu: {result}");
            }
        }
    }


