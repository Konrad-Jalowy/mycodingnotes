import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class CountUsers {
    private static final String URL = "jdbc:sqlite:database.db";

    public static void main(String[] args) {
        String sql = "SELECT COUNT(*) AS count FROM users";

        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql);
             ResultSet rs = pstmt.executeQuery()) {

            if (rs.next()) {
                int count = rs.getInt("count");
                System.out.println("Liczba użytkowników: " + count);
            }

        } catch (SQLException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }
}

