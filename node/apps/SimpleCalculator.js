const readline = require("readline");

// Tworzenie interfejsu do wprowadzania danych z terminala
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Funkcja do obliczeń
function calculate(expression) {
  try {
    // Ocena wyrażenia matematycznego
    const result = eval(expression); // Używamy eval do prostych wyrażeń
    if (isNaN(result)) throw new Error("Nieprawidłowe wyrażenie.");
    return result;
  } catch (error) {
    return "Błąd: " + error.message;
  }
}

// Główna pętla kalkulatora
function startCalculator() {
  console.log("Prosty Kalkulator CLI");
  console.log("Wpisz wyrażenie (np. 2 + 2) lub wpisz 'exit', aby zakończyć.");

  rl.on("line", (input) => {
    if (input.toLowerCase() === "exit") {
      console.log("Do widzenia!");
      rl.close();
      return;
    }

    const result = calculate(input);
    console.log("Wynik:", result);
  });
}

// Uruchom kalkulator
startCalculator();
