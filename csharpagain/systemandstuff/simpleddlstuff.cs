namespace ConsoleApp20
{
    using System;
    using System.Runtime.InteropServices;

    class Program
    {
        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        public static extern int MessageBox(IntPtr hWnd, string lpText, string lpCaption, uint uType);

        static void Main()
        {
            // Wyświetlenie prostego okna dialogowego
            string message = "Czy podoba Ci się ten przykład?";
            string title = "Przykład MessageBox";

            // Typ okna: Tak/Nie
            uint type = 0x04; // MB_YESNO

            // Wywołanie MessageBox
            int result = MessageBox(IntPtr.Zero, message, title, type);

            // Interpretacja wyniku
            if (result == 6) // IDYES
            {
                Console.WriteLine("Użytkownik kliknął TAK.");
            }
            else if (result == 7) // IDNO
            {
                Console.WriteLine("Użytkownik kliknął NIE.");
            }
        }
    }
}