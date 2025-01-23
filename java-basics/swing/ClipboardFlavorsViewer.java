import javax.swing.*;
import java.awt.*;
import java.awt.datatransfer.*;


public class ClipboardFlavorsViewer {

    public static void main(String[] args) {
        // Tworzenie głównego okna aplikacji
        JFrame frame = new JFrame("Clipboard Flavors Viewer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);

        // Tworzenie pola tekstowego do wyświetlania wyników
        JTextArea textArea = new JTextArea();
        textArea.setEditable(false);
        textArea.setLineWrap(true);
        textArea.setWrapStyleWord(true);

        // Tworzenie przycisku do odświeżania zawartości schowka
        JButton refreshButton = new JButton("Pokaż dostępne DataFlavor w schowku");

        // Akcja wykonywana po kliknięciu przycisku
        refreshButton.addActionListener(e -> {
            Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
            Transferable contents = clipboard.getContents(null);

            if (contents != null) {
                StringBuilder result = new StringBuilder("Dostępne DataFlavor w schowku:\n");
                DataFlavor[] flavors = contents.getTransferDataFlavors();
                for (DataFlavor flavor : flavors) {
                    result.append("- ").append(flavor.getHumanPresentableName())
                            .append(" (MIME Type: ").append(flavor.getMimeType()).append(")\n");
                }
                textArea.setText(result.toString());
            } else {
                textArea.setText("Schowek jest pusty.");
            }
        });

        // Dodawanie komponentów do okna
        frame.add(new JScrollPane(textArea), BorderLayout.CENTER);
        frame.add(refreshButton, BorderLayout.SOUTH);

        // Wyświetlenie okna
        frame.setVisible(true);
    }
}
