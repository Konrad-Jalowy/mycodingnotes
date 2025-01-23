using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;

namespace Program123
{
    class ClipboardInspector
    {
        // WinAPI funkcja do uzyskania dostępnych formatów w schowku
        [DllImport("user32.dll")]
        private static extern bool OpenClipboard(IntPtr hWndNewOwner);

        [DllImport("user32.dll")]
        private static extern bool CloseClipboard();

        [DllImport("user32.dll")]
        private static extern uint EnumClipboardFormats(uint format);

        [DllImport("user32.dll")]
        private static extern int GetClipboardFormatName(uint format, System.Text.StringBuilder lpszFormatName, int cchMaxCount);

        static void Main()
        {
            Console.WriteLine("Otwieranie schowka...");

            if (!OpenClipboard(IntPtr.Zero))
            {
                Console.WriteLine("Nie można otworzyć schowka.");
                return;
            }

            try
            {
                Console.WriteLine("Dostępne formaty danych w schowku:");

                uint format = 0;
                List<string> formats = new List<string>();

                // Iterowanie przez dostępne formaty
                while ((format = EnumClipboardFormats(format)) != 0)
                {
                    var formatName = new System.Text.StringBuilder(128);
                    if (GetClipboardFormatName(format, formatName, formatName.Capacity) > 0)
                    {
                        formats.Add(formatName.ToString());
                    }
                    else
                    {
                        formats.Add($"Format ID: {format}");
                    }
                }

                // Wyświetlenie formatów
                if (formats.Count > 0)
                {
                    foreach (var f in formats)
                    {
                        Console.WriteLine($"- {f}");
                    }
                }
                else
                {
                    Console.WriteLine("Schowek jest pusty lub nie zawiera obsługiwanych formatów.");
                }
            }
            finally
            {
                CloseClipboard();
            }
        }
    }

}