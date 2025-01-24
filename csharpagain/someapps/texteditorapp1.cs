namespace TextEditorApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Domyślny tekst do edycji
            string text = "Jon Doe 123deleteme";
            Console.WriteLine("Edit the text below. Use Backspace, Arrow keys, and press Enter to save:");

            string editedText = ReadAndEditText(text);

            // Wyświetl wynik po zakończeniu edycji
            Console.WriteLine("\nResult: hello " + editedText);
        }

        private static string ReadAndEditText(string initialValue)
        {
            string text = initialValue;
            int cursorPosition = text.Length; // Początkowa pozycja kursora
            ConsoleKeyInfo key;

            // Wyświetl początkowy tekst
            Console.Write(text);

            while ((key = Console.ReadKey(true)).Key != ConsoleKey.Enter)
            {
                switch (key.Key)
                {
                    case ConsoleKey.LeftArrow:
                        if (cursorPosition > 0)
                        {
                            cursorPosition--;
                            Console.SetCursorPosition(Console.CursorLeft - 1, Console.CursorTop);
                        }
                        break;

                    case ConsoleKey.RightArrow:
                        if (cursorPosition < text.Length)
                        {
                            cursorPosition++;
                            Console.SetCursorPosition(Console.CursorLeft + 1, Console.CursorTop);
                        }
                        break;

                    case ConsoleKey.Backspace:
                        if (cursorPosition > 0)
                        {
                            cursorPosition--;
                            text = text.Remove(cursorPosition, 1);

                            // Przerysowanie tekstu od pozycji kursora
                            Console.SetCursorPosition(Console.CursorLeft - 1, Console.CursorTop);
                            Console.Write(text.Substring(cursorPosition) + " ");
                            Console.SetCursorPosition(Console.CursorLeft - text.Length + cursorPosition - 1, Console.CursorTop);
                        }
                        break;

                    default:
                        if (!char.IsControl(key.KeyChar))
                        {
                            text = text.Insert(cursorPosition, key.KeyChar.ToString());
                            cursorPosition++;

                            // Przerysowanie tekstu od pozycji kursora
                            Console.Write(text.Substring(cursorPosition - 1));
                            Console.SetCursorPosition(Console.CursorLeft - (text.Length - cursorPosition), Console.CursorTop);
                        }
                        break;
                }
            }

            Console.WriteLine(); // Nowa linia po naciśnięciu Enter
            return text;
        }
    }
}

