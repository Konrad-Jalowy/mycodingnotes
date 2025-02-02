#include <stdio.h>
#include <math.h>

// Funkcja do wykonywania obliczeń
double oblicz(double num1, double num2, char operator) {
    switch(operator) {
        case '+': return num1 + num2;
        case '-': return num1 - num2;
        case '*': return num1 * num2;
        case '/':
            if (num2 != 0)
                return num1 / num2;
            else {
                printf("Błąd: Dzielenie przez zero!\n");
                return NAN;
            }
        case '^': return pow(num1, num2); // Potęgowanie
        case '%':
            if ((int)num1 == num1 && (int)num2 == num2)
                return (int)num1 % (int)num2; // Modulo dla liczb całkowitych
            else {
                printf("Błąd: Modulo działa tylko dla liczb całkowitych!\n");
                return NAN;
            }
        default:
            printf("Błąd: Nieznana operacja!\n");
            return NAN;
    }
}

// Funkcja do pobierania liczb od użytkownika
void pobierzLiczby(double *num1, double *num2, char operator) {
    if (operator == 's') {  // Pierwiastek kwadratowy działa tylko dla jednej liczby
        printf("Podaj liczbę: ");
        scanf("%lf", num1);
    } else {
        printf("Podaj dwie liczby: ");
        scanf("%lf %lf", num1, num2);
    }
}

int main() {
    char operator;
    double num1, num2, wynik;

    while (1) {
        printf("\n==== KALKULATOR ====\n");
        printf("Dostępne operacje: +, -, *, /, ^ (potęgowanie), %% (modulo), s (pierwiastek), q (wyjście)\n");
        printf("Wybierz operację: ");
        scanf(" %c", &operator);

        if (operator == 'q') {
            printf("Zamykanie kalkulatora...\n");
            break;
        }

        pobierzLiczby(&num1, &num2, operator);

        if (operator == 's') {
            if (num1 >= 0)
                wynik = sqrt(num1);
            else {
                printf("Błąd: Pierwiastek tylko z liczb nieujemnych!\n");
                continue;
            }
        } else {
            wynik = oblicz(num1, num2, operator);
        }

        if (!isnan(wynik))
            printf("Wynik: %.2lf\n", wynik);
    }

    return 0;
}
