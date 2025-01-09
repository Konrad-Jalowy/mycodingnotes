namespace ConsoleApp18
{
    public static class StringExtensions
    {
        // Rozszerzanie string
        public static string[] ToWords(this string str)
        {
            return string.IsNullOrWhiteSpace(str) ? Array.Empty<string>() : str.Split(' ');
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            string sentence = "Hello world, this is C#!";

            // Użycie metody rozszerzającej
            var words = sentence.ToWords();

            Console.WriteLine(string.Join(", ", words)); // Hello, world,, this, is, C#!
        }
    }
}