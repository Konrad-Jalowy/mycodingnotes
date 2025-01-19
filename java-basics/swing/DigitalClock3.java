import javax.swing.*;
import java.awt.*;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

public class DigitalClock3 {

    private static boolean isRunning = true; // Flaga do kontrolowania zegara
    private static Timer timer;
    private static String currentDate = ""; // Przechowywana aktualna data
    private static String timeFormat = "HH:mm:ss"; // Domyślny format czasu

    public static void main(String[] args) {
        SwingUtilities.invokeLater(DigitalClock3::createAndShowGUI);
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

        // Lista rozwijana z formatami czasu
        JComboBox<String> formatComboBox = new JComboBox<>(new String[]{
                "HH:mm:ss", // Format 24-godzinny
                "hh:mm:ss a" // Format 12-godzinny z AM/PM
        });

        // Panel na przyciski
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());
        buttonPanel.add(startButton);
        buttonPanel.add(stopButton);
        buttonPanel.add(formatComboBox);

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

        // Akcja dla wyboru formatu czasu
        formatComboBox.addActionListener(e -> {
            timeFormat = (String) formatComboBox.getSelectedItem();
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
                        String currentTime = new SimpleDateFormat(timeFormat).format(new Date());
                        timeLabel.setText(currentTime);

                        // Aktualizacja daty tylko, jeśli jest inna niż poprzednia
                        String newDate = new SimpleDateFormat("EEEE, MMMM dd, yyyy").format(new Date());
                        if (!newDate.equals(currentDate)) {
                            currentDate = newDate;
                            dateLabel.setText(currentDate);
                        }
                    });
                }
            }
        }, 0, 1000); // Odświeżanie co 1 sekundę
    }
}
