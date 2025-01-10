interface BankAccount {
    withdraw(amount: number): void;
  }
  
  class RealBankAccount implements BankAccount {
    private balance: number;
  
    constructor(initialBalance: number) {
      this.balance = initialBalance;
    }
  
    withdraw(amount: number): void {
      if (amount <= this.balance) {
        this.balance -= amount;
        console.log(`Withdrawn: $${amount}. Remaining balance: $${this.balance}`);
      } else {
        console.log('Insufficient funds!');
      }
    }
  }
  
  class BankAccountProxy implements BankAccount {
    private realAccount: RealBankAccount;
    private isAuthenticated: boolean = false;
  
    constructor(realAccount: RealBankAccount) {
      this.realAccount = realAccount;
    }
  
    authenticate(password: string): void {
      if (password === "secret") {
        this.isAuthenticated = true;
        console.log("Authentication successful!");
      } else {
        console.log("Authentication failed!");
      }
    }
  
    withdraw(amount: number): void {
      if (this.isAuthenticated) {
        this.realAccount.withdraw(amount);
      } else {
        console.log("Access denied. Please authenticate first.");
      }
    }
  }
  
  // Użycie
  const realAccount = new RealBankAccount(1000);
  const proxyAccount = new BankAccountProxy(realAccount);
  
  proxyAccount.withdraw(100); // Access denied. Please authenticate first.
  proxyAccount.authenticate("wrong-password"); // Authentication failed!
  proxyAccount.authenticate("secret"); // Authentication successful!
  proxyAccount.withdraw(100); // Withdrawn: $100. Remaining balance: $900.
  