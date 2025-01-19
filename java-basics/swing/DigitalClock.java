import javax.swing.*;
import java.awt.*;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

public class DigitalClock {

    private static boolean isRunning = true; // Flaga do kontrolowania zegara
    private static Timer timer;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(DigitalClock::createAndShowGUI);
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Digital Clock");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        // Etykieta wyświetlająca czas
        JLabel timeLabel = new JLabel("", SwingConstants.CENTER);
        timeLabel.setFont(new Font("Arial", Font.BOLD, 30));

        // Przyciski kontrolujące zegar
        JButton startButton = new JButton("Start");
        JButton stopButton = new JButton("Stop");

        // Panel na przyciski
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());
        buttonPanel.add(startButton);
        buttonPanel.add(stopButton);

        // Dodanie komponentów do okna
        frame.setLayout(new BorderLayout());
        frame.add(timeLabel, BorderLayout.CENTER);
        frame.add(buttonPanel, BorderLayout.SOUTH);

        // Aktualizacja czasu co sekundę
        startClock(timeLabel);

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
                startClock(timeLabel);
            }
        });

        frame.setVisible(true);
    }

    private static void startClock(JLabel timeLabel) {
        timer = new Timer(true);
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                if (isRunning) {
                    // Aktualizacja etykiety z czasem
                    SwingUtilities.invokeLater(() -> {
                        String currentTime = new SimpleDateFormat("HH:mm:ss").format(new Date());
                        timeLabel.setText(currentTime);
                    });
                }
            }
        }, 0, 1000); // Odświeżanie co 1 sekundę
    }
}
