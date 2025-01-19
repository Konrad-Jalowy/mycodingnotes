import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Timer;
import java.util.TimerTask;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

public class Stopwatch5 {

    private static boolean isRunning = false;
    private static int elapsedMilliseconds = 0;
    private static Timer timer;
    private static ArrayList<String> laps = new ArrayList<>();

    public static void main(String[] args) {
        SwingUtilities.invokeLater(Stopwatch5::createAndShowGUI);
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
        try {
            // Tworzenie dokumentu XML/HTML
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.newDocument();

            // Tworzenie elementów HTML
            Element html = doc.createElement("html");
            doc.appendChild(html);

            Element head = doc.createElement("head");
            html.appendChild(head);

            Element title = doc.createElement("title");
            title.setTextContent("Stopwatch Export");
            head.appendChild(title);

            Element body = doc.createElement("body");
            html.appendChild(body);

            Element h1 = doc.createElement("h1");
            h1.setTextContent("Stopwatch Summary");
            body.appendChild(h1);

            Element p = doc.createElement("p");
            p.setTextContent("Total Time: " + formatTime(elapsedMilliseconds));
            body.appendChild(p);

            if (!laps.isEmpty()) {
                Element h2 = doc.createElement("h2");
                h2.setTextContent("Laps");
                body.appendChild(h2);

                Element table = doc.createElement("table");
                table.setAttribute("border", "1");
                table.setAttribute("cellspacing", "0");
                table.setAttribute("cellpadding", "5");
                body.appendChild(table);

                Element headerRow = doc.createElement("tr");
                table.appendChild(headerRow);

                Element th1 = doc.createElement("th");
                th1.setTextContent("Lap");
                headerRow.appendChild(th1);

                Element th2 = doc.createElement("th");
                th2.setTextContent("Time");
                headerRow.appendChild(th2);

                for (int i = 0; i < laps.size(); i++) {
                    Element row = doc.createElement("tr");
                    table.appendChild(row);

                    Element lapCell = doc.createElement("td");
                    lapCell.setTextContent("Lap " + (i + 1));
                    row.appendChild(lapCell);

                    Element timeCell = doc.createElement("td");
                    timeCell.setTextContent(laps.get(i));
                    row.appendChild(timeCell);
                }
            }

            // Zapis do pliku
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult(new File(fileName + ".html"));
            transformer.transform(source, result);

            JOptionPane.showMessageDialog(null, "File saved as: " + fileName + ".html", "Export Successful", JOptionPane.INFORMATION_MESSAGE);

            // Opcjonalne otwarcie w domyślnej przeglądarce
            File file = new File(fileName + ".html");
            if (Desktop.isDesktopSupported()) {
                Desktop.getDesktop().browse(file.toURI());
            }
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(null, "Error saving file: " + ex.getMessage(), "Export Error", JOptionPane.ERROR_MESSAGE);
        }
    }
}
