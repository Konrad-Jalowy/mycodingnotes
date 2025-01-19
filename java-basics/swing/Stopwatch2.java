import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.Timer;
import java.util.TimerTask;

public class Stopwatch2 {

    private static boolean isRunning = false;
    private static int elapsedMilliseconds = 0;
    private static Timer timer;
    private static ArrayList<String> laps = new ArrayList<>();

    public static void main(String[] args) {
        SwingUtilities.invokeLater(Stopwatch2::createAndShowGUI);
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Stopwatch");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        // Etykieta wyświetlająca czas
        JLabel timeLabel = new JLabel("00:00:00.000", SwingConstants.CENTER);
        timeLabel.setFont(new Font("Arial", Font.BOLD, 40));

        // Pole tekstowe na okrążenia
        JTextArea lapsArea = new JTextArea(10, 30);
        lapsArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(lapsArea);

        // Przyciski kontrolujące stoper
        JButton startButton = new JButton("Start");
        JButton stopButton = new JButton("Stop");
        JButton resetButton = new JButton("Reset");
        JButton lapButton = new JButton("Lap");

        // Panel na przyciski
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());
        buttonPanel.add(startButton);
        buttonPanel.add(stopButton);
        buttonPanel.add(resetButton);
        buttonPanel.add(lapButton);

        // Dodanie komponentów do okna
        frame.setLayout(new BorderLayout());
        frame.add(timeLabel, BorderLayout.NORTH);
        frame.add(scrollPane, BorderLayout.CENTER);
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
            elapsedMilliseconds = 0;
            laps.clear();
            timeLabel.setText("00:00:00.000");
            lapsArea.setText("");
        });

        // Akcja dla przycisku Lap
        lapButton.addActionListener(e -> {
            if (isRunning) {
                String lapTime = formatTime(elapsedMilliseconds);
                laps.add(lapTime);
                lapsArea.append("Lap " + laps.size() + ": " + lapTime + "\n");
            }
        });

        frame.setVisible(true);
    }

    private static void startStopwatch(JLabel timeLabel) {
        timer = new Timer(true);
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                if (isRunning) {
                    elapsedMilliseconds += 10;
                    SwingUtilities.invokeLater(() -> {
                        timeLabel.setText(formatTime(elapsedMilliseconds));
                    });
                }
            }
        }, 0, 10); // Odświeżanie co 10 ms
    }

    private static String formatTime(int totalMilliseconds) {
        int hours = totalMilliseconds / 3600000;
        int minutes = (totalMilliseconds % 3600000) / 60000;
        int seconds = (totalMilliseconds % 60000) / 1000;
        int milliseconds = totalMilliseconds % 1000;
        return String.format("%02d:%02d:%02d.%03d", hours, minutes, seconds, milliseconds);
    }
}
