import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TextInputHelloWorld {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Hello World Text Input");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(400, 200);

            JTextField textField = new JTextField(20);
            JButton button = new JButton("Greet Me!");

            button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    String name = textField.getText().trim();
                    if (!name.isEmpty()) {
                        JOptionPane.showMessageDialog(frame, "Hello " + name + "!", "Greeting", JOptionPane.INFORMATION_MESSAGE);
                    } else {
                        JOptionPane.showMessageDialog(frame, "Please enter your name.", "Warning", JOptionPane.WARNING_MESSAGE);
                    }
                }
            });

            JPanel panel = new JPanel();
            panel.add(new JLabel("Enter your name:"));
            panel.add(textField);
            panel.add(button);

            frame.add(panel);
            frame.setVisible(true);
        });
    }
}
