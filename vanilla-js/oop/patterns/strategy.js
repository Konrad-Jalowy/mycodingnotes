// Interfejs strategii - w JS nie mamy interfejsów jak w Pythonie, ale konwencję ustalamy przez strukturę
class PaymentStrategy {
    pay(amount) {
      throw new Error("Method 'pay' must be implemented.");
    }
  }
  
  // Konkretne strategie
  class CreditCardPayment extends PaymentStrategy {
    constructor(cardNumber) {
      super();
      this.cardNumber = cardNumber;
    }
  
    pay(amount) {
      console.log(`Paid ${amount} using Credit Card ${this.cardNumber}.`);
    }
  }
  
  class PayPalPayment extends PaymentStrategy {
    constructor(email) {
      super();
      this.email = email;
    }
  
    pay(amount) {
      console.log(`Paid ${amount} using PayPal account ${this.email}.`);
    }
  }
  
  class CryptoPayment extends PaymentStrategy {
    constructor(walletAddress) {
      super();
      this.walletAddress = walletAddress;
    }
  
    pay(amount) {
      console.log(`Paid ${amount} using Crypto wallet ${this.walletAddress}.`);
    }
  }
  
  // Klasa kontekstowa, która korzysta z różnych strategii
  class PaymentContext {
    constructor(strategy) {
      this.strategy = strategy; // Ustawiamy strategię przy inicjalizacji
    }
  
    setStrategy(strategy) {
      this.strategy = strategy; // Możliwość zmiany strategii w trakcie działania
    }
  
    executePayment(amount) {
      this.strategy.pay(amount); // Delegacja do strategii
    }
  }
  
  // Przykład użycia
  const creditCard = new CreditCardPayment("1234-5678-9012-3456");
  const paypal = new PayPalPayment("user@example.com");
  const crypto = new CryptoPayment("1A2B3C4D5E6F7G8H9I0J");
  
  const payment = new PaymentContext(creditCard);
  payment.executePayment(100); // Paid 100 using Credit Card 1234-5678-9012-3456.
  
  payment.setStrategy(paypal);
  payment.executePayment(200); // Paid 200 using PayPal account user@example.com.
  
  payment.setStrategy(crypto);
  payment.executePayment(300); // Paid 300 using Crypto wallet 1A2B3C4D5E6F7G8H9I0J.
  