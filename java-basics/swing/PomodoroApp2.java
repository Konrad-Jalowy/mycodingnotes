import javax.swing.*;
import java.awt.*;
import java.util.Timer;
import java.util.TimerTask;

public class PomodoroApp2 {

    private static int workDuration = 25 * 60; // Default 25 minutes
    private static int shortBreakDuration = 5 * 60; // Default 5 minutes
    private static int longBreakDuration = 15 * 60; // Default 15 minutes

    private static int timeLeft = workDuration; // Remaining time in the current phase
    private static boolean isRunning = false;
    private static int pomodoroCount = 0; // Number of completed pomodoros
    private static Timer timer;
    private static String currentPhase = "Work"; // Current phase

    public static void main(String[] args) {
        SwingUtilities.invokeLater(PomodoroApp2::createAndShowGUI);
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Pomodoro Timer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        JLabel timerLabel = new JLabel(formatTime(timeLeft), SwingConstants.CENTER);
        timerLabel.setFont(new Font("Arial", Font.BOLD, 40));

        JLabel phaseLabel = new JLabel("Phase: Work", SwingConstants.CENTER);
        phaseLabel.setFont(new Font("Arial", Font.PLAIN, 20));

        JLabel pomodoroCounter = new JLabel("Pomodoros: 0", SwingConstants.CENTER);
        pomodoroCounter.setFont(new Font("Arial", Font.PLAIN, 16));

        JButton startButton = new JButton("Start");
        JButton stopButton = new JButton("Stop");
        JButton resetButton = new JButton("Reset");
        JButton settingsButton = new JButton("Settings");

        JPanel buttonPanel = new JPanel(new FlowLayout());
        buttonPanel.add(startButton);
        buttonPanel.add(stopButton);
        buttonPanel.add(resetButton);
        buttonPanel.add(settingsButton);

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
            timeLeft = workDuration;
            currentPhase = "Work";
            pomodoroCount = 0;
            timerLabel.setText(formatTime(timeLeft));
            phaseLabel.setText("Phase: Work");
            pomodoroCounter.setText("Pomodoros: 0");
        });

        settingsButton.addActionListener(e -> openSettingsDialog(frame));

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
                                    timeLeft = longBreakDuration;
                                } else {
                                    currentPhase = "Short Break";
                                    timeLeft = shortBreakDuration;
                                }
                            } else {
                                currentPhase = "Work";
                                timeLeft = workDuration;
                            }
                            phaseLabel.setText("Phase: " + currentPhase);
                            showNotification(currentPhase);
                        });
                    }
                }
            }
        }, 0, 1000); // Refresh every second
    }

    private static void openSettingsDialog(JFrame parent) {
        JDialog settingsDialog = new JDialog(parent, "Settings", true);
        settingsDialog.setSize(300, 200);
        settingsDialog.setLayout(new GridLayout(4, 2, 10, 10));

        settingsDialog.add(new JLabel("Work Duration (min):"));
        JTextField workField = new JTextField(String.valueOf(workDuration / 60));
        settingsDialog.add(workField);

        settingsDialog.add(new JLabel("Short Break (min):"));
        JTextField shortBreakField = new JTextField(String.valueOf(shortBreakDuration / 60));
        settingsDialog.add(shortBreakField);

        settingsDialog.add(new JLabel("Long Break (min):"));
        JTextField longBreakField = new JTextField(String.valueOf(longBreakDuration / 60));
        settingsDialog.add(longBreakField);

        JButton saveButton = new JButton("Save");
        saveButton.addActionListener(e -> {
            try {
                workDuration = Integer.parseInt(workField.getText()) * 60;
                shortBreakDuration = Integer.parseInt(shortBreakField.getText()) * 60;
                longBreakDuration = Integer.parseInt(longBreakField.getText()) * 60;
                timeLeft = workDuration;
                JOptionPane.showMessageDialog(settingsDialog, "Settings saved successfully!", "Success", JOptionPane.INFORMATION_MESSAGE);
                settingsDialog.dispose();
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(settingsDialog, "Invalid input. Please enter valid numbers.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        });
        settingsDialog.add(saveButton);

        settingsDialog.setVisible(true);
    }

    private static String formatTime(int seconds) {
        int minutes = seconds / 60;
        int secs = seconds % 60;
        return String.format("%02d:%02d", minutes, secs);
    }

    private static void showNotification(String phase) {
        JOptionPane.showMessageDialog(null, "Time to switch to: " + phase, "Pomodoro Notification", JOptionPane.INFORMATION_MESSAGE);
    }
}
