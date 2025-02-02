package org.example;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseManager2 {
    private static final String URL = "jdbc:sqlite:database.db";

    public static Connection connect() {
        try {
            return DriverManager.getConnection(URL);
        } catch (SQLException e) {
            System.out.println("Błąd połączenia z bazą danych: " + e.getMessage());
            return null;
        }
    }

    public static void createTable() {
        String sql = "CREATE TABLE IF NOT EXISTS users (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                "name TEXT NOT NULL, " +
                "age INTEGER NOT NULL)";
        try (Connection conn = connect();
             var stmt = conn.createStatement()) {
            stmt.execute(sql);
            System.out.println("Tabela `users` została utworzona!");
        } catch (SQLException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        createTable();
    }
}
