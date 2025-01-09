namespace ConsoleApp18
{
    public delegate string TextProcessor(string input);

    class Program
    {
        static string RemoveSpecialCharacters(string input) =>
            new string(input.Where(char.IsLetterOrDigit).ToArray());

        static string ToLowerCase(string input) => input.ToLower();

        static string TrimWhiteSpaces(string input) => input.Trim();

        static void Main()
        {
            TextProcessor processor = RemoveSpecialCharacters;
            processor += ToLowerCase;
            processor += TrimWhiteSpaces;

            string input = "  Hello, World!  ";
            string result = Pipe(processor, input);

            Console.WriteLine(result);  // Wynik: "helloworld"
        }

        static string Pipe(TextProcessor processor, string input)
        {
            foreach (var method in processor.GetInvocationList())
            {
                input = ((TextProcessor)method)(input);
            }
            return input;
        }
    }
}