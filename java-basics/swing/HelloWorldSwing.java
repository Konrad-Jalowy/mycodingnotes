import javax.swing.*;

public class HelloWorldSwing {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Hello World App");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(300, 200);

            JLabel label = new JLabel("Hello World", SwingConstants.CENTER);
            frame.add(label);

            frame.setVisible(true);
        });
    }
}
