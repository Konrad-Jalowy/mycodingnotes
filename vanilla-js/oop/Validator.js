class Validator {
    constructor() {
      this.rules = [];
    }
  
    addRule(rule) {
      this.rules.push(rule);
    }
  
    validate(data) {
      return this.rules.every(rule => rule(data));
    }
  }
  
  // Reguły walidacji
  const notEmpty = data => data.trim().length > 0;
  const minLength = min => data => data.length >= min;
  const maxLength = max => data => data.length <= max;
  const containsDigit = data => /\d/.test(data);
  
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
  