namespace ConsoleApp18
{
    using System;

    public interface IValidationStrategy
    {
        bool Validate(string value);
    }

    public class EmailValidation : IValidationStrategy
    {
        public bool Validate(string value)
        {
            return value.Contains("@") && value.Contains(".");
        }
    }

    public class PhoneValidation : IValidationStrategy
    {
        public bool Validate(string value)
        {
            return long.TryParse(value, out _) && value.Length == 9;
        }
    }

    public class Validator
    {
        private readonly IValidationStrategy _strategy;

        public Validator(IValidationStrategy strategy)
        {
            _strategy = strategy;
        }

        public bool Validate(string value)
        {
            return _strategy.Validate(value);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Validator emailValidator = new Validator(new EmailValidation());
            Console.WriteLine(emailValidator.Validate("test@example.com")); // True

            Validator phoneValidator = new Validator(new PhoneValidation());
            Console.WriteLine(phoneValidator.Validate("123456789")); // True
        }
    }

}