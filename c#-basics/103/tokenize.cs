using System;
using System.Text.RegularExpressions;

class Program {
    static void Main() {
        string expression = "3 + 5 * (2 - 8)";
        var tokens = Regex.Matches(expression, @"\d+|\+|\-|\*|\/|\(|\)");
        foreach (var token in tokens) {
            Console.WriteLine(token);
        }
        // Output: 3, +, 5, *, (, 2, -, 8, )
    }
}
