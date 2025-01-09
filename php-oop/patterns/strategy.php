<?php
// Interfejs strategii
interface PaymentStrategy {
    public function pay($amount);
}

// Konkretne strategie
class CreditCardPayment implements PaymentStrategy {
    private $cardNumber;

    public function __construct($cardNumber) {
        $this->cardNumber = $cardNumber;
    }

    public function pay($amount) {
        echo "Paid $amount using Credit Card {$this->cardNumber}.\n";
    }
}

class PayPalPayment implements PaymentStrategy {
    private $email;

    public function __construct($email) {
        $this->email = $email;
    }

    public function pay($amount) {
        echo "Paid $amount using PayPal account {$this->email}.\n";
    }
}

class CryptoPayment implements PaymentStrategy {
    private $walletAddress;

    public function __construct($walletAddress) {
        $this->walletAddress = $walletAddress;
    }

    public function pay($amount) {
        echo "Paid $amount using Crypto wallet {$this->walletAddress}.\n";
    }
}

// Klasa kontekstowa, która korzysta z różnych strategii
class PaymentContext {
    private $strategy;

    public function __construct(PaymentStrategy $strategy) {
        $this->strategy = $strategy;
    }

    public function setStrategy(PaymentStrategy $strategy) {
        $this->strategy = $strategy;
    }

    public function executePayment($amount) {
        $this->strategy->pay($amount);
    }
}

// Przykład użycia
$creditCard = new CreditCardPayment("1234-5678-9012-3456");
$paypal = new PayPalPayment("user@example.com");
$crypto = new CryptoPayment("1A2B3C4D5E6F7G8H9I0J");

$payment = new PaymentContext($creditCard);
$payment->executePayment(100); // Paid 100 using Credit Card 1234-5678-9012-3456.

$payment->setStrategy($paypal);
$payment->executePayment(200); // Paid 200 using PayPal account user@example.com.

$payment->setStrategy($crypto);
$payment->executePayment(300); // Paid 300 using Crypto wallet 1A2B3C4D5E6F7G8H9I0J.