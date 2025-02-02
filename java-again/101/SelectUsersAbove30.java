
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class SelectUsersAbove30 {
    private static final String URL = "jdbc:sqlite:database.db";

    public static void main(String[] args) {
        String sql = "SELECT * FROM users WHERE age > ?";

        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setInt(1, 30); // Ustawiamy parametr w zapytaniu
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") +
                        ", Imię: " + rs.getString("name") +
                        ", Wiek: " + rs.getInt("age"));
            }

        } catch (SQLException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }
}
