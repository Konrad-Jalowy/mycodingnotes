import javax.swing.*;
import java.awt.*;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Timer;
import java.util.TimerTask;

public class Stopwatch3 {

    private static boolean isRunning = false;
    private static int elapsedMilliseconds = 0;
    private static Timer timer;
    private static ArrayList<String> laps = new ArrayList<>();

    public static void main(String[] args) {
        SwingUtilities.invokeLater(Stopwatch3::createAndShowGUI);
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Stopwatch");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);

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
        JButton exportButton = new JButton("Export to HTML");

        // Panel na przyciski
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());
        buttonPanel.add(startButton);
        buttonPanel.add(stopButton);
        buttonPanel.add(resetButton);
        buttonPanel.add(lapButton);
        buttonPanel.add(exportButton);

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

        // Akcja dla przycisku Export
        exportButton.addActionListener(e -> {
            String fileName = JOptionPane.showInputDialog(frame, "Enter file name (without extension):", "Export to HTML", JOptionPane.PLAIN_MESSAGE);
            if (fileName != null && !fileName.trim().isEmpty()) {
                exportToHTML(fileName.trim());
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

    private static void exportToHTML(String fileName) {
        File file = new File(fileName + ".html");
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(file))) {
            writer.write("<html>\n<head>\n<title>Stopwatch Export</title>\n</head>\n<body>\n");
            writer.write("<h1>Stopwatch Summary</h1>\n");
            writer.write("<p><strong>Total Time:</strong> " + formatTime(elapsedMilliseconds) + "</p>\n");

            if (!laps.isEmpty()) {
                writer.write("<h2>Laps</h2>\n<table border='1' cellspacing='0' cellpadding='5'>\n");
                writer.write("<tr><th>Lap</th><th>Time</th></tr>\n");
                for (int i = 0; i < laps.size(); i++) {
                    writer.write("<tr><td>Lap " + (i + 1) + "</td><td>" + laps.get(i) + "</td></tr>\n");
                }
                writer.write("</table>\n");
            }

            writer.write("</body>\n</html>");
            JOptionPane.showMessageDialog(null, "File saved as: " + file.getAbsolutePath(), "Export Successful", JOptionPane.INFORMATION_MESSAGE);

            // Opcjonalne otwarcie w domyślnej przeglądarce
            if (Desktop.isDesktopSupported()) {
                Desktop.getDesktop().browse(file.toURI());
            }
        } catch (IOException ex) {
            JOptionPane.showMessageDialog(null, "Error saving file: " + ex.getMessage(), "Export Error", JOptionPane.ERROR_MESSAGE);
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(null, "Error opening file: " + ex.getMessage(), "Export Error", JOptionPane.ERROR_MESSAGE);
        }
    }
}
