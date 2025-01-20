
import javax.swing.*;
import java.awt.*;
import java.util.Timer;
import java.util.TimerTask;

public class PomodoroApp {

    private static final int WORK_DURATION = 25 * 60; // 25 minut w sekundach
    private static final int SHORT_BREAK = 5 * 60; // 5 minut w sekundach
    private static final int LONG_BREAK = 15 * 60; // 15 minut w sekundach

    private static int timeLeft = WORK_DURATION; // Czas pozostały w bieżącej fazie
    private static boolean isRunning = false;
    private static int pomodoroCount = 0; // Liczba ukończonych pomodorów
    private static Timer timer;
    private static String currentPhase = "Work"; // Aktualna faza

    public static void main(String[] args) {
        SwingUtilities.invokeLater(PomodoroApp::createAndShowGUI);
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Pomodoro Timer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        JLabel timerLabel = new JLabel(formatTime(timeLeft), SwingConstants.CENTER);
        timerLabel.setFont(new Font("Arial", Font.BOLD, 40));

        JLabel phaseLabel = new JLabel("Phase: Work", SwingConstants.CENTER);
        phaseLabel.setFont(new Font("Arial", Font.PLAIN, 20));

        JLabel pomodoroCounter = new JLabel("Pomodoros: 0", SwingConstants.CENTER);
        pomodoroCounter.setFont(new Font("Arial", Font.PLAIN, 16));

        JButton startButton = new JButton("Start");
        JButton stopButton = new JButton("Stop");
        JButton resetButton = new JButton("Reset");

        JPanel buttonPanel = new JPanel(new FlowLayout());
        buttonPanel.add(startButton);
        buttonPanel.add(stopButton);
        buttonPanel.add(resetButton);

        frame.setLayout(new BorderLayout());
        frame.add(timerLabel, BorderLayout.NORTH);
        frame.add(phaseLabel, BorderLayout.CENTER);
        frame.add(pomodoroCounter, BorderLayout.SOUTH);
        frame.add(buttonPanel, BorderLayout.PAGE_END);

        startButton.addActionListener(e -> {
            if (!isRunning) {
                isRunning = true;
                startTimer(timerLabel, phaseLabel, pomodoroCounter);
            }
        });

        stopButton.addActionListener(e -> {
            if (isRunning) {
                isRunning = false;
                if (timer != null) {
                    timer.cancel();
                }
            }
        });

        resetButton.addActionListener(e -> {
            isRunning = false;
            if (timer != null) {
                timer.cancel();
            }
            timeLeft = WORK_DURATION;
            currentPhase = "Work";
            pomodoroCount = 0;
            timerLabel.setText(formatTime(timeLeft));
            phaseLabel.setText("Phase: Work");
            pomodoroCounter.setText("Pomodoros: 0");
        });

        frame.setVisible(true);
    }

    private static void startTimer(JLabel timerLabel, JLabel phaseLabel, JLabel pomodoroCounter) {
        timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                if (isRunning) {
                    timeLeft--;

                    SwingUtilities.invokeLater(() -> timerLabel.setText(formatTime(timeLeft)));

                    if (timeLeft <= 0) {
                        SwingUtilities.invokeLater(() -> {
                            if (currentPhase.equals("Work")) {
                                pomodoroCount++;
                                pomodoroCounter.setText("Pomodoros: " + pomodoroCount);
                                if (pomodoroCount % 4 == 0) {
                                    currentPhase = "Long Break";
                                    timeLeft = LONG_BREAK;
                                } else {
                                    currentPhase = "Short Break";
                                    timeLeft = SHORT_BREAK;
                                }
                            } else {
                                currentPhase = "Work";
                                timeLeft = WORK_DURATION;
                            }
                            phaseLabel.setText("Phase: " + currentPhase);
                        });
                    }
                }
            }
        }, 0, 1000); // Odświeżanie co sekundę
    }

    private static String formatTime(int seconds) {
        int minutes = seconds / 60;
        int secs = seconds % 60;
        return String.format("%02d:%02d", minutes, secs);
    }
}