public class MenuSystem {
    public static void main(String[] args) {
        // Funkcje akcji (można użyć lambd):
        Runnable showUsers = () -> System.out.println("Wyświetlam listę użytkowników (Java)...");
        Runnable addUser = () -> System.out.println("Dodaję użytkownika (Java)...");
        Runnable advancedSearch = () -> System.out.println("Wyszukiwanie zaawansowane (Java)...");

        // Główne menu
        Menu mainMenu = new Menu("Główne menu (Java)");

        // Dodajemy akcje
        mainMenu.addSimpleAction(
                "[1] Wyświetl użytkowników",
                new String[] { "1", "show_users" },
                showUsers
        );
        mainMenu.addSimpleAction(
                "[2] Dodaj użytkownika",
                new String[] { "2", "add_user" },
                addUser
        );

        // Sub-menu
        Menu searchMenu = new Menu("Sub-menu wyszukiwania (Java)");
        searchMenu.addSimpleAction(
                "[1] Wyszukiwanie zaawansowane",
                new String[] { "1", "advanced" },
                advancedSearch
        );
        // Wyjście z sub-menu
        searchMenu.addExitAction("[b] Powrót", new String[] { "b", "back" });

        // Dodajemy sub-menu do głównego menu
        mainMenu.addSubmenu(
                "[3] Wejdź w menu wyszukiwania",
                new String[] { "3", "search" },
                searchMenu
        );

        // Akcja wyjścia z głównego menu
        mainMenu.addExitAction("[q] Zakończ", new String[] { "q", "quit" });

        // Uruchamiamy menu
        mainMenu.run();
    }
}