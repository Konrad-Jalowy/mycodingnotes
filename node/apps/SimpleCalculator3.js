import readline from "readline";
import chalk from "chalk";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const history = [];

// Funkcja do bardziej szczegółowej weryfikacji
function isValidExpression(expression) {
  const basicRegex = /^[0-9+\-*/().\s]+$/; // Podstawowa weryfikacja
  if (!basicRegex.test(expression)) {
    return { valid: false, error: "Wyrażenie zawiera niedozwolone znaki." };
  }

  // Sprawdzanie podwójnych operatorów
  if (/[\+\-\*/]{2,}/.test(expression)) {
    return { valid: false, error: "Wyrażenie zawiera podwójne operatory, np. ++, **, itp." };
  }

  // Sprawdzanie operatora na końcu
  if (/[\+\-\*/]$/.test(expression)) {
    return { valid: false, error: "Wyrażenie nie może kończyć się operatorem." };
  }

  // Sprawdzanie nieprawidłowych liczb (np. 1..2 lub 2.2.2)
  if (/\d+\.\d*\./.test(expression)) {
    return { valid: false, error: "Wyrażenie zawiera nieprawidłową liczbę z wieloma kropkami." };
  }

  // Jeśli wszystkie sprawdzenia przeszły, wyrażenie jest poprawne
  return { valid: true, error: null };
}

// Funkcja do obliczeń
function calculate(expression) {
  try {
    const validation = isValidExpression(expression);
    if (!validation.valid) {
      throw new Error(validation.error);
    }

    const result = eval(expression);
    if (isNaN(result)) throw new Error("Nie można obliczyć wyniku.");
    return result;
  } catch (error) {
    return chalk.red("Błąd: " + error.message);
  }
}

// Główna funkcja kalkulatora
function startCalculator() {
  console.log(chalk.blue("Prosty Kalkulator CLI"));
  console.log(chalk.green("Wpisz wyrażenie (np. 2 + 2) lub wpisz 'exit', aby zakończyć."));
  console.log(chalk.green("Wpisz 'history', aby zobaczyć historię obliczeń."));

  rl.on("line", (input) => {
    const trimmedInput = input.trim().toLowerCase();

    if (trimmedInput === "exit") {
      console.log(chalk.yellow("Do widzenia!"));
      rl.close();
      return;
    }

    if (trimmedInput === "history") {
      if (history.length === 0) {
        console.log(chalk.yellow("Historia jest pusta."));
      } else {
        console.log(chalk.magenta("Historia obliczeń:"));
        history.forEach((entry, index) => {
          console.log(chalk.cyan(`${index + 1}: ${entry}`));
        });
      }
      return;
    }

    const result = calculate(trimmedInput);

    if (typeof result === "number") {
      console.log(chalk.green("Wynik: " + result));
      history.push(`${input} = ${result}`);
    } else {
      console.log(result);
    }
  });
}
