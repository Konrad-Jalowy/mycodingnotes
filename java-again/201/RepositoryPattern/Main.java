package main;

import database.SQLiteConnector;
import model.User;
import repository.UserRepository;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        SQLiteConnector.initializeDatabase();
        UserRepository userRepository = new UserRepository();

        // Dodanie użytkownika
        userRepository.addUser(new User("john_doe", "john@example.com"));
        userRepository.addUser(new User("jane_doe", "jane@example.com"));

        // Pobranie wszystkich użytkowników
        List<User> users = userRepository.getAllUsers();
        users.forEach(System.out::println);

        // Pobranie jednego użytkownika
        userRepository.getUserById(1).ifPresent(System.out::println);

        // Usunięcie użytkownika
        userRepository.deleteUser(1);
    }
}
