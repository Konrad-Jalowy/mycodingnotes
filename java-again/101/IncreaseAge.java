import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class IncreaseAge {
    private static final String URL = "jdbc:sqlite:database.db";

    public static void main(String[] args) {
        String sql = "UPDATE users SET age = age + 1";

        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            int rowsUpdated = pstmt.executeUpdate();
            System.out.println("Zmieniono wiek dla " + rowsUpdated + " użytkowników.");

        } catch (SQLException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }
}