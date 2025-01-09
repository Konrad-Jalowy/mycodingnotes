type ValidationRule = (data: string) => boolean;

class Validator {
  private rules: ValidationRule[] = [];

  addRule(rule: ValidationRule): void {
    this.rules.push(rule);
  }

  validate(data: string): boolean {
    return this.rules.every(rule => rule(data));
  }
}

// Reguły walidacji
const notEmpty: ValidationRule = data => data.trim().length > 0;
const minLength = (min: number): ValidationRule => data => data.length >= min;
const maxLength = (max: number): ValidationRule => data => data.length <= max;
const containsDigit: ValidationRule = data => /\d/.test(data);

// Tworzenie walidatora
const validator = new Validator();
validator.addRule(notEmpty);
validator.addRule(minLength(5));
validator.addRule(maxLength(10));
validator.addRule(containsDigit);

// Testy
console.log(validator.validate("12345")); // True
console.log(validator.validate("12"));    // False (za krótkie)
console.log(validator.validate("12345678901")); // False (za długie)
console.log(validator.validate("abcde")); // False (brak cyfry)