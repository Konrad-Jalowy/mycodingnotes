using System;
using System.Text.RegularExpressions;

class Program {
    static void Main() {
        string pattern = @"\d+";
        string text = "Znajdź liczby 42 i 123 w tym tekście.";

        MatchCollection matches = Regex.Matches(text, pattern);
        foreach (Match match in matches) {
            Console.WriteLine(match.Value);
        }
        // Output:
        // 42
        // 123
    }
}
