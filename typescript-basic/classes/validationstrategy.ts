interface ValidationStrategy {
    validate(value: string): boolean;
}

class EmailValidation implements ValidationStrategy {
    validate(value: string): boolean {
        return value.includes("@") && value.includes(".");
    }
}

class PhoneValidation implements ValidationStrategy {
    validate(value: string): boolean {
        return /^\d{9}$/.test(value);
    }
}

class Validator {
    private strategy: ValidationStrategy;

    constructor(strategy: ValidationStrategy) {
        this.strategy = strategy;
    }

    validate(value: string): boolean {
        return this.strategy.validate(value);
    }
}

// Użycie
const emailValidator = new Validator(new EmailValidation());
console.log(emailValidator.validate("test@example.com")); // true

const phoneValidator = new Validator(new PhoneValidation());
console.log(phoneValidator.validate("123456789")); // true
