package org.example;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseManager {
    private static final String URL = "jdbc:sqlite:database.db";

    public static Connection connect() {
        try {
            return DriverManager.getConnection(URL);
        } catch (SQLException e) {
            System.out.println("Błąd połączenia z bazą danych: " + e.getMessage());
            return null;
        }
    }

    public static void main(String[] args) {
        Connection conn = connect();
        if (conn != null) {
            System.out.println("Połączono z SQLite!");
        }
    }
}
