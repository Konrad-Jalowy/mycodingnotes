#include <stdio.h>
#include <math.h>

// Funkcja wykonująca obliczenia
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
        case '^': return pow(num1, num2);
        case '%':
            if ((int)num1 == num1 && (int)num2 == num2)
                return (int)num1 % (int)num2;
            else {
                printf("Błąd: Modulo działa tylko dla liczb całkowitych!\n");
                return NAN;
            }
        default:
            printf("Błąd: Nieznana operacja!\n");
            return NAN;
    }
}

int main() {
    char operator;
    double num1, num2, wynik;

    while (1) {
        printf("\n==== KALKULATOR ====\n");
        printf("Podaj pierwszą liczbę (lub 'q' aby wyjść): ");

        if (scanf("%lf", &num1) != 1) {
            printf("Zamykanie kalkulatora...\n");
            break;
        }

        printf("Wybierz operację (+, -, *, /, ^, %%): ");
        scanf(" %c", &operator);

        printf("Podaj drugą liczbę: ");
        scanf("%lf", &num2);

        wynik = oblicz(num1, num2, operator);

        if (!isnan(wynik)) {
            printf("Wynik: %.2lf %c %.2lf = %.2lf\n", num1, operator, num2, wynik);
        }
    }

    return 0;
}
