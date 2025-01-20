import javax.swing.*;
import java.awt.*;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.Locale;

public class DaysUntilNewYear {

    public static void main(String[] args) {
        // Force English locale
        Locale.setDefault(new Locale("en", "US"));

        // Set up the frame
        JFrame frame = new JFrame("Days Until New Year");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);

        // Create a label to display the result
        JLabel label = new JLabel("", SwingConstants.CENTER);
        label.setFont(new Font("Segoe UI", Font.BOLD, 18));

        // Calculate the days until New Year
        int daysLeft = calculateDaysUntilNewYear();
        label.setText("Days until New Year: " + daysLeft);

        // Add label to frame
        frame.add(label);

        // Display the frame
        frame.setVisible(true);
    }

    private static int calculateDaysUntilNewYear() {
        LocalDate today = LocalDate.now();
        LocalDate newYear = LocalDate.of(today.getYear() + 1, 1, 1);

        // Calendar-based approach
        int daysLeft = (int) ChronoUnit.DAYS.between(today, newYear);
        if (!today.equals(newYear.minusDays(1))) {
            daysLeft++;
        }

        return daysLeft;
    }
}
