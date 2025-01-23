namespace Program123
{
    using System;
    using System.Runtime.InteropServices;
    using System.Text;

    class ClipboardInspector
    {
        [DllImport("user32.dll")]
        private static extern bool OpenClipboard(IntPtr hWndNewOwner);

        [DllImport("user32.dll")]
        private static extern bool CloseClipboard();

        [DllImport("user32.dll")]
        private static extern uint EnumClipboardFormats(uint format);

        [DllImport("user32.dll")]
        private static extern int GetClipboardFormatName(uint format, StringBuilder lpszFormatName, int cchMaxCount);

        [DllImport("user32.dll")]
        private static extern IntPtr GetClipboardData(uint uFormat);

        static void Main()
        {
            if (!OpenClipboard(IntPtr.Zero))
            {
                Console.WriteLine("Nie można otworzyć schowka.");
                return;
            }

            try
            {
                bool chromiumFormatFound = false;
                uint format = 0;

                // Iterowanie przez formaty w schowku
                while ((format = EnumClipboardFormats(format)) != 0)
                {
                    var formatName = new StringBuilder(128);
                    if (GetClipboardFormatName(format, formatName, formatName.Capacity) > 0)
                    {
                        if (formatName.ToString() == "Chromium internal source URL")
                        {
                            chromiumFormatFound = true;

                            // Odczyt URL źródła
                            IntPtr handle = GetClipboardData(format);
                            if (handle != IntPtr.Zero)
                            {
                                string sourceUrl = Marshal.PtrToStringAnsi(handle);
                                Console.WriteLine($"Chromium Source URL: {sourceUrl}");
                            }
                            else
                            {
                                Console.WriteLine("Nie można odczytać URL źródła.");
                            }
                        }
                    }
                }

                if (!chromiumFormatFound)
                {
                    Console.WriteLine("Format Chromium internal source URL nie został znaleziony.");
                }

                // Próba odczytania tekstu z schowka
                if (OpenClipboard(IntPtr.Zero))
                {
                    uint unicodeFormat = 13; // CF_UNICODETEXT
                    IntPtr textHandle = GetClipboardData(unicodeFormat);
                    if (textHandle != IntPtr.Zero)
                    {
                        string text = Marshal.PtrToStringUni(textHandle);
                        Console.WriteLine($"Tekst w schowku: {text}");
                    }
                    else
                    {
                        Console.WriteLine("Nie można odczytać tekstu z schowka.");
                    }
                }
            }
            finally
            {
                CloseClipboard();
            }
        }
    }

}