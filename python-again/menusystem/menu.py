import re
from typing import Callable, List, Union, Pattern


class MenuAction:
    """
    Pojedyncza akcja menu.
    trigger może być:
      - str  -> np. "q"
      - List[str] -> np. ["q", "quit"]
      - Pattern (regex) -> re.compile(...)
      - Callable[[str], bool] -> np. funkcja sprawdzająca warunek
    action to funkcja, która zostanie wywołana, gdy input wpasuje się w trigger
    prompt to tekst opisujący akcję (wyświetlany w menu)
    """

    def __init__(self,
                 prompt: str,
                 trigger: Union[str, List[str], Pattern, Callable[[str], bool]],
                 action: Callable[[], None]):
        self.prompt = prompt
        self.trigger = trigger
        self.action = action

    def matches(self, user_input: str) -> bool:
        """
        Sprawdza, czy dany user_input pasuje do definicji triggera.
        """
        if isinstance(self.trigger, str):
            return user_input == self.trigger
        elif isinstance(self.trigger, list):
            return user_input in self.trigger
        elif isinstance(self.trigger, re.Pattern):
            return bool(self.trigger.match(user_input))
        elif callable(self.trigger):
            return self.trigger(user_input)
        return False


class Menu:
    """
    Klasa reprezentująca menu tekstowe z pętlą wejścia.
    """

    def __init__(self,
                 title: str,
                 quiet: bool = False,
                 prompt: str = "Wybierz akcję: "):
        """
        :param title: Tytuł wyświetlany nad menu (można np. nie wyświetlać w ogóle, jeśli wolimy).
        :param quiet: Czy menu ma być w trybie cichym (nie wyświetlać listy akcji za każdym razem).
        :param prompt: Tekst, który pojawi się przy wczytywaniu inputu.
        """
        self.title = title
        self.actions: List[MenuAction] = []
        self.is_running = False
        self.quiet = quiet
        self.prompt_text = prompt

    def add_action(self, action: MenuAction):
        """
        Dodaje nową akcję do menu.
        """
        self.actions.append(action)

    def add_simple_action(self,
                          prompt: str,
                          trigger: Union[str, List[str], Pattern, Callable[[str], bool]],
                          func: Callable[[], None]):
        """
        Syntactic sugar do łatwiejszego dodania akcji bez tworzenia obiektu MenuAction.
        """
        action = MenuAction(prompt, trigger, func)
        self.actions.append(action)

    def add_submenu(self,
                    prompt: str,
                    trigger: Union[str, List[str], Pattern, Callable[[str], bool]],
                    submenu: 'Menu'):
        """
        Dodaje sub-menu jako akcję. Po wybraniu danej akcji wejdziemy w pętlę submenu.
        """

        def open_submenu():
            # Uruchamiamy submenu (zwróć uwagę, że to blokujący call, wrócimy po wyjściu z submenu)
            submenu.run()

        self.add_simple_action(prompt, trigger, open_submenu)

    def add_exit_action(self,
                        prompt: str,
                        trigger: Union[str, List[str], Pattern, Callable[[str], bool]]):
        """
        Akcja kończąca pracę menu.
        """

        def exit_menu():
            print("Zakończono działanie menu.")
            self.is_running = False

        self.add_simple_action(prompt, trigger, exit_menu)

    def display(self):
        """
        Wyświetla tytuł oraz listę akcji (o ile tryb nie jest cichy).
        """
        if not self.quiet:
            print("\n=== " + self.title + " ===")
            for action in self.actions:
                print(f"[{self._extract_trigger_text(action.trigger)}] {action.prompt}")

    def _extract_trigger_text(self, trigger) -> str:
        """
        Pomocnicza metoda do wyświetlania w menu "co wpisujemy",
        choćby w przypadku prostego stringa lub listy stringów.
        """
        if isinstance(trigger, str):
            return trigger
        elif isinstance(trigger, list):
            return "|".join(trigger)
        elif isinstance(trigger, re.Pattern):
            return trigger.pattern
        elif callable(trigger):
            return "func_trigger"
        return str(trigger)

    def run(self):
        """
        Uruchamia główną pętlę menu.
        """
        self.is_running = True
        while self.is_running:
            self.display()
            user_input = input(self.prompt_text).strip()
            # Szukamy akcji, która pasuje do user_input
            matched_action = None
            for action in self.actions:
                if action.matches(user_input):
                    matched_action = action
                    break
            if matched_action:
                matched_action.action()
            else:
                print(f"Nieznana komenda: {user_input}")


# Przykład użycia:
if __name__ == "__main__":
    # Stwórzmy proste funkcje do akcji menu
    def show_users():
        print("Wyświetlam listę użytkowników... (tu logika aplikacji)")


    def add_user():
        print("Dodawanie nowego użytkownika... (tu logika aplikacji)")


    def advanced_search():
        print("Wyszukiwanie zaawansowane... (tu logika aplikacji)")


    # Tworzymy główne menu
    main_menu = Menu(title="Główne menu")

    # Dodajemy akcje
    main_menu.add_simple_action(
        prompt="Wyświetl użytkowników",
        trigger=["1", "show_users"],
        func=show_users
    )
    main_menu.add_simple_action(
        prompt="Dodaj użytkownika",
        trigger=["2", "add_user"],
        func=add_user
    )

    # Dodajmy sub-menu, np. do operacji wyszukiwania
    search_menu = Menu(title="Menu wyszukiwania")
    search_menu.add_simple_action(
        prompt="Wyszukiwanie zaawansowane",
        trigger=["1", "advanced"],
        func=advanced_search
    )
    # Akcja wyjścia z sub-menu:
    search_menu.add_exit_action(
        prompt="Powrót",
        trigger=["b", "back"]
    )

    # Dodajemy sub-menu do głównego menu
    main_menu.add_submenu(
        prompt="Wejdź w menu wyszukiwania",
        trigger=["3", "search"],
        submenu=search_menu
    )

    # Dodajemy akcję wyjścia z głównego menu
    main_menu.add_exit_action(
        prompt="Zakończ",
        trigger=["q", "quit"]
    )

    # Uruchamiamy menu
    main_menu.run()
