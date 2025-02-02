import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class CheckUserExists {
    private static final String URL = "jdbc:sqlite:database.db";

    public static void main(String[] args) {
        int userId = 2; // ID użytkownika do sprawdzenia
        String sql = "SELECT EXISTS(SELECT 1 FROM users WHERE id = ?) AS user_exists";

        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setInt(1, userId);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next() && rs.getInt("user_exists") == 1) {
                System.out.println("Użytkownik o ID " + userId + " istnieje.");
            } else {
                System.out.println("Użytkownik o ID " + userId + " nie istnieje.");
            }

        } catch (SQLException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }
}
