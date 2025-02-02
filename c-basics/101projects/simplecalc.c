#include <stdio.h>

int main() {
    char operator;
    double num1, num2, result;

    // Wybór operacji
    printf("Prosty kalkulator\n");
    printf("Wybierz operację: (+, -, *, /): ");
    scanf(" %c", &operator);

    // Pobranie liczb od użytkownika
    printf("Podaj dwie liczby: ");
    scanf("%lf %lf", &num1, &num2);

    // Wykonanie operacji
    switch(operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 != 0)
                result = num1 / num2;
            else {
                printf("Błąd: Dzielenie przez zero!\n");
                return 1;
            }
            break;
        default:
            printf("Błąd: Nieznana operacja!\n");
            return 1;
    }

    // Wyświetlenie wyniku
    printf("Wynik: %.2lf\n", result);

    return 0;
}