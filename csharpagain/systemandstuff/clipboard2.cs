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
                Console.WriteLine("Dostępne formaty danych w schowku:");
                uint format = 0;
                while ((format = EnumClipboardFormats(format)) != 0)
                {
                    var formatName = new StringBuilder(128);
                    if (GetClipboardFormatName(format, formatName, formatName.Capacity) > 0)
                    {
                        Console.WriteLine($"- {formatName} (ID: {format})");

                        // Odczyt danych RTF
                        if (formatName.ToString().Equals("Rich Text Format"))
                        {
                            IntPtr handle = GetClipboardData(format);
                            if (handle != IntPtr.Zero)
                            {
                                string rtfContent = GetRichTextData(handle);
                                Console.WriteLine($"  Zawartość RTF: {rtfContent}");
                            }
                            else
                            {
                                Console.WriteLine("  Nie można odczytać danych RTF.");
                            }
                        }
                    }
                    else
                    {
                        Console.WriteLine($"- Format ID: {format}");
                    }
                }
            }
            finally
            {
                CloseClipboard();
            }
        }

        private static string GetRichTextData(IntPtr handle)
        {
            // Zakładamy, że dane RTF są przechowywane w kodowaniu ASCII
            try
            {
                byte[] buffer = Marshal.PtrToStructure<byte[]>(handle);
                return Encoding.ASCII.GetString(buffer);
            }
            catch
            {
                return "Nie można zdekodować danych RTF.";
            }
        }
    }

}