import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        // Utworzenie głównego okna (JFrame)
        JFrame frame = new JFrame("Hello World App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        // Dodanie etykiety (JLabel) z napisem "Hello, World!"
        JLabel label = new JLabel("Hello, World!", SwingConstants.CENTER);
        frame.add(label);

        // Wyświetlenie okna
        frame.setVisible(true);
    }
}
