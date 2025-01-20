import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;
import java.awt.Toolkit;

public class TextInputHelloWorld {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Hello World Text Input");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(400, 200);

            JTextField textField = new JTextField(20);
            JButton button = new JButton("Copy to Clipboard");

            button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    String text = textField.getText().trim();
                    if (!text.isEmpty()) {
                        StringSelection selection = new StringSelection(text);
                        Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
                        clipboard.setContents(selection, null);
                        JOptionPane.showMessageDialog(frame, "Text copied to clipboard!", "Success", JOptionPane.INFORMATION_MESSAGE);
                    } else {
                        JOptionPane.showMessageDialog(frame, "Please enter some text to copy.", "Warning", JOptionPane.WARNING_MESSAGE);
                    }
                }
            });

            JPanel panel = new JPanel();
            panel.add(new JLabel("Enter your text:"));
            panel.add(textField);
            panel.add(button);

            frame.add(panel);
            frame.setVisible(true);
        });
    }
}
