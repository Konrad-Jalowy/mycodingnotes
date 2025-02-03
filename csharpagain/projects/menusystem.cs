using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

public class MenuAction
{
    public string Prompt { get; }
    private Func<string, bool> Trigger { get; }
    private Action ActionMethod { get; }

    public MenuAction(string prompt, Func<string, bool> trigger, Action actionMethod)
    {
        Prompt = prompt;
        Trigger = trigger;
        ActionMethod = actionMethod;
    }

    public bool Matches(string input) => Trigger(input);

    public void Run() => ActionMethod();
}

public class Menu
{
    private string Title { get; }
    private bool Quiet { get; }
    private string PromptText { get; }
    private List<MenuAction> Actions { get; }
    private bool isRunning;

    public Menu(string title, bool quiet = false, string prompt = "Wybierz akcję: ")
    {
        Title = title;
        Quiet = quiet;
        PromptText = prompt;
        Actions = new List<MenuAction>();
    }

    public void AddAction(MenuAction action)
    {
        Actions.Add(action);
    }

    /// <summary>
    /// Pomocnicza metoda do tworzenia akcji z listą triggerów typu string.
    /// </summary>
    public void AddSimpleAction(string prompt, string[] triggers, Action actionMethod)
    {
        Func<string, bool> trig = input =>
        {
            foreach (var t in triggers)
            {
                if (input.Equals(t, StringComparison.OrdinalIgnoreCase))
                    return true;
            }
            return false;
        };
        Actions.Add(new MenuAction(prompt, trig, actionMethod));
    }

    /// <summary>
    /// Dodanie sub-menu.
    /// </summary>
    public void AddSubmenu(string prompt, string[] triggers, Menu submenu)
    {
        Func<string, bool> trig = input =>
        {
            foreach (var t in triggers)
            {
                if (input.Equals(t, StringComparison.OrdinalIgnoreCase))
                    return true;
            }
            return false;
        };

        MenuAction submenuAction = new MenuAction(
            prompt,
            trig,
            () => submenu.Run()
        );
        Actions.Add(submenuAction);
    }

    /// <summary>
    /// Dodanie akcji wyjścia (zakończenia pętli).
    /// </summary>
    public void AddExitAction(string prompt, string[] triggers)
    {
        Func<string, bool> trig = input =>
        {
            foreach (var t in triggers)
            {
                if (input.Equals(t, StringComparison.OrdinalIgnoreCase))
                    return true;
            }
            return false;
        };

        MenuAction exitAction = new MenuAction(
            prompt,
            trig,
            () => Stop()
        );
        Actions.Add(exitAction);
    }

    public void Run()
    {
        isRunning = true;
        while (isRunning)
        {
            if (!Quiet)
                Display();

            Console.Write(PromptText);
            string userInput = Console.ReadLine()?.Trim() ?? "";

            bool found = false;
            foreach (var action in Actions)
            {
                if (action.Matches(userInput))
                {
                    action.Run();
                    found = true;
                    break;
                }
            }
            if (!found)
            {
                Console.WriteLine("Nieznana komenda: " + userInput);
            }
        }
    }

    public void Stop()
    {
        isRunning = false;
        Console.WriteLine("Zakończono działanie menu.");
    }

    private void Display()
    {
        Console.WriteLine("\n=== " + Title + " ===");
        foreach (var action in Actions)
        {
            Console.WriteLine(action.Prompt);
        }
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        // Proste funkcje do demonstracji
        void ShowUsers() => Console.WriteLine("Wyświetlam listę użytkowników (C#)...");
        void AddUser() => Console.WriteLine("Dodawanie użytkownika (C#)...");
        void AdvancedSearch() => Console.WriteLine("Wyszukiwanie zaawansowane (C#)...");

        // Główne menu
        var mainMenu = new Menu("Główne Menu (C#)");

        // Dodajemy akcje
        mainMenu.AddSimpleAction(
            "[1] Wyświetl użytkowników",
            new[] { "1", "show_users" },
            ShowUsers
        );
        mainMenu.AddSimpleAction(
            "[2] Dodaj użytkownika",
            new[] { "2", "add_user" },
            AddUser
        );

        // Sub-menu do wyszukiwania
        var searchMenu = new Menu("Sub-menu wyszukiwania (C#)");
        searchMenu.AddSimpleAction(
            "[1] Wyszukiwanie zaawansowane",
            new[] { "1", "advanced" },
            AdvancedSearch
        );
        // Wyjście z sub-menu
        searchMenu.AddExitAction("[b] Powrót", new[] { "b", "back" });

        // Dodajemy sub-menu
        mainMenu.AddSubmenu(
            "[3] Wejdź w menu wyszukiwania",
            new[] { "3", "search" },
            searchMenu
        );

        // Akcja wyjścia z głównego menu
        mainMenu.AddExitAction("[q] Zakończ", new[] { "q", "quit" });

        // Uruchamiamy menu
        mainMenu.Run();
    }
}
