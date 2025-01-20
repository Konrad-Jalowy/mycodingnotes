import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ButtonHelloWorld {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Hello World Button App");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(300, 200);

            JButton button = new JButton("Click Me!");
            JButton resetButton = new JButton("Reset");
            JLabel label = new JLabel("", SwingConstants.CENTER);

            button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    if (label.getText().isEmpty()) {
                        label.setText("Hello World");
                    } else {
                        JOptionPane.showMessageDialog(
                                frame,
                                "Hello World has already been set!",
                                "Information",
                                JOptionPane.INFORMATION_MESSAGE
                        );
                    }
                }
            });

            resetButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    label.setText("");
                }
            });

            frame.setLayout(new BoxLayout(frame.getContentPane(), BoxLayout.Y_AXIS));
            frame.add(button);
            frame.add(resetButton);
            frame.add(label);

            frame.setVisible(true);
        });
    }
}
