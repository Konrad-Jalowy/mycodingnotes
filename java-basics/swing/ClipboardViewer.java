import javax.swing.*;
import java.awt.*;
import java.awt.datatransfer.*;
import java.io.IOException;

public class ClipboardViewer {

    public static void main(String[] args) {
        JFrame frame = new JFrame("Clipboard Viewer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        JTextArea textArea = new JTextArea();
        JButton refreshButton = new JButton("Odśwież");

        refreshButton.addActionListener(e -> {
            Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
            try {
                Transferable contents = clipboard.getContents(null);
                if (contents != null && contents.isDataFlavorSupported(DataFlavor.stringFlavor)) {
                    String data = (String) contents.getTransferData(DataFlavor.stringFlavor);
                    textArea.setText(data);
                } else {
                    textArea.setText("Brak tekstu w schowku.");
                }
            } catch (UnsupportedFlavorException | IOException ex) {
                textArea.setText("Błąd podczas odczytu schowka: " + ex.getMessage());
            }
        });

        frame.add(new JScrollPane(textArea), BorderLayout.CENTER);
        frame.add(refreshButton, BorderLayout.SOUTH);
        frame.setVisible(true);
    }
}
