class Validator {
    constructor(rules) {
      this.rules = rules; // Zasady walidacji
    }
  
    // Funkcja walidacji
    validate(data) {
      const errors = {};
  
      for (const [field, value] of Object.entries(data)) {
        const fieldRules = this.rules[field];
        if (!fieldRules) continue; // Jeśli brak reguł, pomijamy pole
  
        // Walidacja reguł
        for (const [rule, ruleValue] of Object.entries(fieldRules)) {
          const isValid = this[rule](value, ruleValue);
          if (!isValid) {
            errors[field] = errors[field] || [];
            errors[field].push(this.getErrorMessage(field, rule, ruleValue));
          }
        }
      }
  
      return { isValid: Object.keys(errors).length === 0, errors };
    }
  
    // Walidacje
    required(value) {
      return value !== null && value !== undefined && value !== '';
    }
  
    email(value) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(value);
    }
  
    minLength(value, min) {
      return typeof value === 'string' && value.length >= min;
    }
  
    maxLength(value, max) {
      return typeof value === 'string' && value.length <= max;
    }
  
    pattern(value, regex) {
      return regex.test(value);
    }
  
    // Funkcja do generowania komunikatów o błędach
    getErrorMessage(field, rule, ruleValue) {
      const messages = {
        required: `${field} is required.`,
        email: `${field} must be a valid email address.`,
        minLength: `${field} must be at least ${ruleValue} characters long.`,
        maxLength: `${field} must be at most ${ruleValue} characters long.`,
        pattern: `${field} is invalid.`
      };
  
      return messages[rule] || `${field} failed the ${rule} validation.`;
    }
  }
  
  // Przykładowe testy
  const validator = new Validator({
    name: { required: true, minLength: 3 },
    email: { required: true, email: true },
    password: { required: true, minLength: 6, maxLength: 20 }
  });
  
  const formData = {
    name: 'Jo',
    email: 'invalid-email',
    password: '123'
  };
  
  const result = validator.validate(formData);
  
  if (!result.isValid) {
    console.log('Errors:', result.errors);
  } else {
    console.log('Validation passed!');
  }
  