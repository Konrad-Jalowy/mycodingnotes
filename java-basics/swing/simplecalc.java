import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class simplecalc{
    public static void main(String[] args) {
        // Utworzenie głównego okna (JFrame)
        JFrame frame = new JFrame("Kalkulator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);
        frame.setLayout(new GridLayout(4, 2, 10, 10)); // Siatka 4x2 z odstępami

        // Pola tekstowe do wprowadzania liczb
        JTextField num1Field = new JTextField();
        JTextField num2Field = new JTextField();

        // Etykiety
        JLabel num1Label = new JLabel("Liczba 1:");
        JLabel num2Label = new JLabel("Liczba 2:");
        JLabel resultLabel = new JLabel("Wynik:");
        JLabel resultValue = new JLabel("");

        // Przycisk do obliczeń
        JButton calculateButton = new JButton("Oblicz");

        // Dodawanie komponentów do okna
        frame.add(num1Label);
        frame.add(num1Field);
        frame.add(num2Label);
        frame.add(num2Field);
        frame.add(calculateButton);
        frame.add(resultLabel);
        frame.add(resultValue);

        // Obsługa zdarzeń - kliknięcie przycisku
        calculateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    // Pobranie liczb z pól tekstowych
                    double num1 = Double.parseDouble(num1Field.getText());
                    double num2 = Double.parseDouble(num2Field.getText());

                    // Obliczenie wyniku
                    double result = num1 + num2;

                    // Wyświetlenie wyniku
                    resultValue.setText(String.valueOf(result));
                } catch (NumberFormatException ex) {
                    // Obsługa błędu, gdy użytkownik nie wpisze liczby
                    JOptionPane.showMessageDialog(frame, "Proszę wprowadzić poprawne liczby.", "Błąd", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        // Wyświetlenie okna
        frame.setVisible(true);
    }
}
