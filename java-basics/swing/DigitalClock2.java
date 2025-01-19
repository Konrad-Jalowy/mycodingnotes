import javax.swing.*;
import java.awt.*;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

public class DigitalClock2 {

    private static boolean isRunning = true; // Flaga do kontrolowania zegara
    private static Timer timer;
    private static boolean is24HourFormat = true; // Flaga formatu czasu

    public static void main(String[] args) {
        SwingUtilities.invokeLater(DigitalClock2::createAndShowGUI);
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Digital Clock");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        // Etykieta wyświetlająca czas i datę
        JLabel timeLabel = new JLabel("", SwingConstants.CENTER);
        timeLabel.setFont(new Font("Arial", Font.BOLD, 30));

        JLabel dateLabel = new JLabel("", SwingConstants.CENTER);
        dateLabel.setFont(new Font("Arial", Font.PLAIN, 20));

        // Przyciski kontrolujące zegar
        JButton startButton = new JButton("Start");
        JButton stopButton = new JButton("Stop");
        JButton toggleFormatButton = new JButton("Change Format");

        // Panel na przyciski
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());
        buttonPanel.add(startButton);
        buttonPanel.add(stopButton);
        buttonPanel.add(toggleFormatButton);

        // Dodanie komponentów do okna
        frame.setLayout(new BorderLayout());
        frame.add(timeLabel, BorderLayout.CENTER);
        frame.add(dateLabel, BorderLayout.NORTH);
        frame.add(buttonPanel, BorderLayout.SOUTH);

        // Aktualizacja czasu i daty co sekundę
        startClock(timeLabel, dateLabel);

        // Akcja dla przycisku Stop
        stopButton.addActionListener(e -> {
            if (isRunning) {
                isRunning = false;
                if (timer != null) {
                    timer.cancel();
                }
            }
        });

        // Akcja dla przycisku Start
        startButton.addActionListener(e -> {
            if (!isRunning) {
                isRunning = true;
                startClock(timeLabel, dateLabel);
            }
        });

        // Akcja dla przycisku zmiany formatu
        toggleFormatButton.addActionListener(e -> {
            is24HourFormat = !is24HourFormat;
        });

        frame.setVisible(true);
    }

    private static void startClock(JLabel timeLabel, JLabel dateLabel) {
        timer = new Timer(true);
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                if (isRunning) {
                    SwingUtilities.invokeLater(() -> {
                        // Aktualizacja czasu
                        String timeFormat = is24HourFormat ? "HH:mm:ss" : "hh:mm:ss a";
                        String currentTime = new SimpleDateFormat(timeFormat).format(new Date());
                        timeLabel.setText(currentTime);

                        // Aktualizacja daty
                        String currentDate = new SimpleDateFormat("EEEE, MMMM dd, yyyy").format(new Date());
                        dateLabel.setText(currentDate);
                    });
                }
            }
        }, 0, 1000); // Odświeżanie co 1 sekundę
    }
}
