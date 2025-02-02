import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class DatabaseInitializer {
    private static final String URL = "jdbc:sqlite:todo.db";

    public static void createTable() {
        String sql = """
                CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
                )""";

        try (Connection conn = DriverManager.getConnection(URL);
             Statement stmt = conn.createStatement()) {
            stmt.execute(sql);
            System.out.println("Baza danych gotowa.");
        } catch (Exception e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }
}
