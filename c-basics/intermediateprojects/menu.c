#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Ustalmy maksymalną liczbę akcji i maksymalną długość inputu.
#define MAX_ACTIONS 10
#define MAX_INPUT_LENGTH 100

// Definicja typów funkcji dla triggera i akcji:
typedef bool (*trigger_func_t)(const char*);
typedef void (*action_func_t)(void*);

// Struktura opisująca jedną akcję w menu
typedef struct {
    char prompt[100];        // Tekst wyświetlany w menu, np. "[1] Pokaż użytkowników"
    trigger_func_t trigger;  // Funkcja sprawdzająca wpis (czy pasuje do tej akcji)
    action_func_t action;    // Funkcja, która ma się wykonać
    void* context;           // Kontekst, np. wskaźnik do Menu lub innych danych
} MenuAction;

// Deklaracja struktury Menu (zawiera tablicę akcji, pętlę główną, itd.)
typedef struct Menu {
    char title[100];             // Tytuł menu
    bool quiet;                  // Czy menu ma być w trybie cichym
    char promptText[50];         // Tekst "Wybierz akcję: "
    MenuAction actions[MAX_ACTIONS];
    int actionCount;             // Ile akcji aktualnie jest zarejestrowanych
    bool isRunning;              // Czy menu jest obecnie w pętli
} Menu;

// -------------------------------
// Deklaracje funkcji związanych z Menu
void initMenu(Menu* menu, const char* title, bool quiet, const char* promptText);
void addAction(Menu* menu, const char* prompt, trigger_func_t trig, action_func_t act, void* ctx);
void runMenu(Menu* menu);
void displayMenu(const Menu* menu);

// -------------------------------
// Funkcja pomocnicza sprawdzająca, czy `input` równa się któremuś ze stringów w `variants`
bool trigger_multi(const char* input, int n, const char** variants) {
    for(int i = 0; i < n; i++) {
        // Porównanie zwykłe (case-sensitive); można zmienić na strcasecmp, jeśli chcemy ignorować wielkość liter
        if(strcmp(input, variants[i]) == 0) {
            return true;
        }
    }
    return false;
}

// -------------------------------
// PRZYKŁADOWE TRIGGERS:
bool trigger_show(const char* input) {
    const char* variants[] = { "1", "show_users" };
    return trigger_multi(input, 2, variants);
}

bool trigger_add(const char* input) {
    const char* variants[] = { "2", "add_user" };
    return trigger_multi(input, 2, variants);
}

bool trigger_submenu(const char* input) {
    const char* variants[] = { "3", "search" };
    return trigger_multi(input, 2, variants);
}

bool trigger_exit_main(const char* input) {
    const char* variants[] = { "q", "quit" };
    return trigger_multi(input, 2, variants);
}

bool trigger_back(const char* input) {
    const char* variants[] = { "b", "back" };
    return trigger_multi(input, 2, variants);
}

bool trigger_adv(const char* input) {
    const char* variants[] = { "1", "advanced" };
    return trigger_multi(input, 2, variants);
}

// -------------------------------
// PRZYKŁADOWE ACTIONS:
void show_users_action(void* context) {
    printf("Wyświetlam listę użytkowników (C)...\n");
}

void add_user_action(void* context) {
    printf("Dodaję użytkownika (C)...\n");
}

void advanced_search_action(void* context) {
    printf("Wyszukiwanie zaawansowane (C)...\n");
}

// Akcja otwierająca sub-menu (context to wskaźnik do innego Menu)
void open_submenu_action(void* context) {
    if(context == NULL) return;
    Menu* submenu = (Menu*)context;
    runMenu(submenu);
}

// Akcja wyjścia z menu - ustawia isRunning = false
void exit_menu_action(void* context) {
    if(context == NULL) return;
    Menu* menu = (Menu*)context;
    menu->isRunning = false;
    printf("Zamykam menu: %s\n", menu->title);
}

// -------------------------------
// IMPLEMENTACJA FUNKCJI MENU:

void initMenu(Menu* menu, const char* title, bool quiet, const char* promptText) {
    // title
    strncpy(menu->title, title, sizeof(menu->title) - 1);
    menu->title[sizeof(menu->title) - 1] = '\0';

    // quiet
    menu->quiet = quiet;

    // prompt
    strncpy(menu->promptText, promptText, sizeof(menu->promptText) - 1);
    menu->promptText[sizeof(menu->promptText) - 1] = '\0';

    // Inicjalnie brak akcji, menu nie jest w pętli
    menu->actionCount = 0;
    menu->isRunning = false;
}

void addAction(Menu* menu, const char* prompt, trigger_func_t trig, action_func_t act, void* ctx) {
    // Sprawdźmy, czy jest jeszcze miejsce w tablicy
    if(menu->actionCount >= MAX_ACTIONS) {
        fprintf(stderr, "Brak miejsca na więcej akcji w menu!\n");
        return;
    }
    // Wskaźnik do wolnego miejsca
    MenuAction* action = &menu->actions[menu->actionCount];
    // Zapis prompt
    strncpy(action->prompt, prompt, sizeof(action->prompt) - 1);
    action->prompt[sizeof(action->prompt) - 1] = '\0';

    // Wskaźniki na funkcje:
    action->trigger = trig;
    action->action = act;
    action->context = ctx;

    menu->actionCount++;
}

void displayMenu(const Menu* menu) {
    if(!menu->quiet) {
        printf("\n=== %s ===\n", menu->title);
        for(int i = 0; i < menu->actionCount; i++) {
            printf("%s\n", menu->actions[i].prompt);
        }
    }
}

// Główna pętla menu
void runMenu(Menu* menu) {
    menu->isRunning = true;
    while(menu->isRunning) {
        displayMenu(menu);

        printf("%s", menu->promptText);
        char userInput[MAX_INPUT_LENGTH];
        if(!fgets(userInput, MAX_INPUT_LENGTH, stdin)) {
            // Błąd lub EOF
            return;
        }
        // Usuwamy ewentualne \n
        userInput[strcspn(userInput, "\n")] = 0;

        bool found = false;
        for(int i = 0; i < menu->actionCount; i++) {
            if(menu->actions[i].trigger(userInput)) {
                menu->actions[i].action(menu->actions[i].context);
                found = true;
                break;
            }
        }
        if(!found) {
            printf("Nieznana komenda: %s\n", userInput);
        }
    }
}

// -------------------------------
// PRZYKŁAD UŻYCIA W FUNKCJI main
int main() {
    // Tworzymy główne menu
    Menu mainMenu;
    initMenu(&mainMenu, "Główne menu (C)", false, "Wybierz akcję: ");

    // Dodajemy akcje do głównego menu
    addAction(&mainMenu, "[1] Wyświetl użytkowników", trigger_show, show_users_action, NULL);
    addAction(&mainMenu, "[2] Dodaj użytkownika", trigger_add, add_user_action, NULL);

    // Tworzymy sub-menu
    Menu searchMenu;
    initMenu(&searchMenu, "Sub-menu wyszukiwania (C)", false, "Wybierz akcję (sub): ");

    // Dodajemy akcje w sub-menu
    addAction(&searchMenu, "[1] Wyszukiwanie zaawansowane", trigger_adv, advanced_search_action, NULL);
    // Akcja powrotu z sub-menu
    addAction(&searchMenu, "[b] Powrót", trigger_back, exit_menu_action, &searchMenu);

    // Dodajemy akcję otwierającą sub-menu w menu głównym
    addAction(&mainMenu, "[3] Wejdź w menu wyszukiwania", trigger_submenu, open_submenu_action, &searchMenu);

    // Dodajemy akcję wyjścia z głównego menu
    addAction(&mainMenu, "[q] Zakończ", trigger_exit_main, exit_menu_action, &mainMenu);

    // Uruchamiamy główne menu
    runMenu(&mainMenu);

    return 0;
}
