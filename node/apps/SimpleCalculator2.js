import readline from "readline";
import chalk from "chalk";

// Tworzenie interfejsu do wprowadzania danych z terminala
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Historia obliczeń
const history = [];

// Funkcja do weryfikacji wejścia
function isValidExpression(expression) {
  const regex = /^[0-9+\-*/().\s]+$/;
  return regex.test(expression);
}

// Funkcja do obliczeń
function calculate(expression) {
  try {
    if (!isValidExpression(expression)) {
      throw new Error("Nieprawidłowe wyrażenie matematyczne.");
    }
    const result = eval(expression);
    if (isNaN(result)) throw new Error("Nie można obliczyć wyniku.");
    return result;
  } catch (error) {
    return chalk.red("Błąd: " + error.message);
  }
}

// Główna pętla kalkulatora
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
      console.log(result); // Wyświetla błąd (czerwony tekst)
    }
  });
}

// Uruchom kalkulator
startCalculator();
