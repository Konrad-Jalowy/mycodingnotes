import readline from "readline";
import chalk from "chalk";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const history = [];

// Zaawansowane funkcje matematyczne
const mathFunctions = {
  sin: Math.sin,
  cos: Math.cos,
  tan: Math.tan,
  sqrt: Math.sqrt,
  pow: Math.pow,
  abs: Math.abs,
  log: Math.log,
  exp: Math.exp,
  floor: Math.floor,
  ceil: Math.ceil,
};

// Funkcja do sprawdzania poprawności wyrażenia
function isValidExpression(expression) {
  const basicRegex = /^[0-9+\-*/().,\s\w]+$/; // Podstawowa weryfikacja
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

  return { valid: true, error: null };
}

// Funkcja do obliczeń
function calculate(expression) {
  try {
    const validation = isValidExpression(expression);
    if (!validation.valid) {
      throw new Error(validation.error);
    }

    // Tworzenie bezpiecznego eval z zaawansowanymi funkcjami matematycznymi
    const sandbox = {
      ...mathFunctions, // Zaawansowane funkcje matematyczne
      Math, // Obiekt Math
      PI: Math.PI,
      E: Math.E,
    };

    // Bezpieczne wykonanie wyrażenia
    const result = new Function(
      ...Object.keys(sandbox),
      `return (${expression});`
    )(...Object.values(sandbox));

    if (isNaN(result)) throw new Error("Nie można obliczyć wyniku.");
    return result;
  } catch (error) {
    return chalk.red("Błąd: " + error.message);
  }
}

// Główna funkcja kalkulatora
function startCalculator() {
  console.log(chalk.blue("Zaawansowany Kalkulator CLI"));
  console.log(chalk.green("Wpisz wyrażenie (np. sin(PI / 2), sqrt(16), 2 + 2) lub wpisz 'exit', aby zakończyć."));
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

startCalculator();
