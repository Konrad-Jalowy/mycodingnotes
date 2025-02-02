import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class SelectUsersOrdered {
    private static final String URL = "jdbc:sqlite:database.db";

    public static void main(String[] args) {
        String sql = "SELECT * FROM users ORDER BY age ASC"; // Sortowanie rosnąco

        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql);
             ResultSet rs = pstmt.executeQuery()) {

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
