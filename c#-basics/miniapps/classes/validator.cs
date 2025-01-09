namespace ConsoleApp18
{
    class Validator
    {
        private readonly List<Func<string, bool>> _rules = new();

        public Validator AddRule(Func<string, bool> rule)
        {
            _rules.Add(rule);
            return this;
        }

        public bool Validate(string data)
        {
            return _rules.All(rule => rule(data));
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Func<string, bool> NotEmpty = data => !string.IsNullOrWhiteSpace(data);
            Func<int, Func<string, bool>> MinLength = min => data => data.Length >= min;
            Func<int, Func<string, bool>> MaxLength = max => data => data.Length <= max;
            Func<string, bool> ContainsDigit = data => data.Any(char.IsDigit);

            // Tworzenie walidatora
            var validator = new Validator()
                .AddRule(NotEmpty)
                .AddRule(MinLength(5))
                .AddRule(MaxLength(10))
                .AddRule(ContainsDigit);

            // Testy
            Console.WriteLine(validator.Validate("12345")); // True
            Console.WriteLine(validator.Validate("12"));    // False (za krótkie)
            Console.WriteLine(validator.Validate("12345678901")); // False (za długie)
            Console.WriteLine(validator.Validate("abcde")); // False (brak cyfry)
        }
    }
}