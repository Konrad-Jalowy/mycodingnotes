import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DeleteYoungUsers {
    private static final String URL = "jdbc:sqlite:database.db";

    public static void main(String[] args) {
        String sql = "DELETE FROM users WHERE age < ?";

        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setInt(1, 25); // Usuwamy użytkowników poniżej 25 lat
            int rowsAffected = pstmt.executeUpdate();
            System.out.println("Usunięto " + rowsAffected + " użytkowników.");

        } catch (SQLException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }
}
