import javax.swing.*;
import java.awt.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.Locale;
import java.util.Timer;
import java.util.TimerTask;

public class DaysUntilNewYear2 {

    public static void main(String[] args) {
        // Force English locale
        Locale.setDefault(new Locale("en", "US"));

        // Set up the frame
        JFrame frame = new JFrame("Days Until New Year");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLayout(new BorderLayout());

        // Create a label to display the days until New Year
        JLabel daysLabel = new JLabel("", SwingConstants.CENTER);
        daysLabel.setFont(new Font("Segoe UI", Font.BOLD, 18));

        // Calculate the days until New Year
        int daysLeft = calculateDaysUntilNewYear();
        daysLabel.setText("Days until New Year: " + daysLeft);

        // Create a label to display the countdown timer
        JLabel timerLabel = new JLabel("", SwingConstants.CENTER);
        timerLabel.setFont(new Font("Segoe UI", Font.PLAIN, 16));

        // Start the countdown timer
        startCountdownTimer(timerLabel);

        // Add labels to the frame
        frame.add(daysLabel, BorderLayout.NORTH);
        frame.add(timerLabel, BorderLayout.CENTER);

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

    private static void startCountdownTimer(JLabel timerLabel) {
        Timer timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                LocalDateTime now = LocalDateTime.now();
                LocalDateTime newYear = LocalDateTime.of(now.getYear() + 1, 1, 1, 0, 0);

                long hours = ChronoUnit.HOURS.between(now, newYear);
                long minutes = ChronoUnit.MINUTES.between(now, newYear) % 60;
                long seconds = ChronoUnit.SECONDS.between(now, newYear) % 60;

                timerLabel.setText(String.format("Time until New Year: %02d:%02d:%02d", hours, minutes, seconds));
            }
        }, 0, 1000);
    }
}
