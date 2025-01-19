import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Timer;
import java.util.TimerTask;

public class Stopwatch {

    private static boolean isRunning = false;
    private static int elapsedSeconds = 0;
    private static Timer timer;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(Stopwatch::createAndShowGUI);
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Stopwatch");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        // Etykieta wyświetlająca czas
        JLabel timeLabel = new JLabel("00:00:00", SwingConstants.CENTER);
        timeLabel.setFont(new Font("Arial", Font.BOLD, 40));

        // Przyciski kontrolujące stoper
        JButton startButton = new JButton("Start");
        JButton stopButton = new JButton("Stop");
        JButton resetButton = new JButton("Reset");

        // Panel na przyciski
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());
        buttonPanel.add(startButton);
        buttonPanel.add(stopButton);
        buttonPanel.add(resetButton);

        // Dodanie komponentów do okna
        frame.setLayout(new BorderLayout());
        frame.add(timeLabel, BorderLayout.CENTER);
        frame.add(buttonPanel, BorderLayout.SOUTH);

        // Akcja dla przycisku Start
        startButton.addActionListener(e -> {
            if (!isRunning) {
                isRunning = true;
                startStopwatch(timeLabel);
            }
        });

        // Akcja dla przycisku Stop
        stopButton.addActionListener(e -> {
            if (isRunning) {
                isRunning = false;
                if (timer != null) {
                    timer.cancel();
                }
            }
        });

        // Akcja dla przycisku Reset
        resetButton.addActionListener(e -> {
            isRunning = false;
            if (timer != null) {
                timer.cancel();
            }
            elapsedSeconds = 0;
            timeLabel.setText("00:00:00");
        });

        frame.setVisible(true);
    }

    private static void startStopwatch(JLabel timeLabel) {
        timer = new Timer(true);
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                if (isRunning) {
                    elapsedSeconds++;
                    SwingUtilities.invokeLater(() -> {
                        timeLabel.setText(formatTime(elapsedSeconds));
                    });
                }
            }
        }, 0, 1000); // Odświeżanie co 1 sekundę
    }

    private static String formatTime(int totalSeconds) {
        int hours = totalSeconds / 3600;
        int minutes = (totalSeconds % 3600) / 60;
        int seconds = totalSeconds % 60;
        return String.format("%02d:%02d:%02d", hours, minutes, seconds);
    }
}
