import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SwingCalculator {
    private JFrame frame;
    private JTextField display;
    private StringBuilder currentInput;
    private String operator;
    private double firstOperand;

    public SwingCalculator() {
        frame = new JFrame("Kalkulator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 400);

        currentInput = new StringBuilder();
        operator = "";
        firstOperand = 0;

        initializeUI();
        frame.setVisible(true);
    }

    private void initializeUI() {
        frame.setLayout(new BorderLayout());

        // Display
        display = new JTextField();
        display.setFont(new Font("Arial", Font.BOLD, 24));
        display.setHorizontalAlignment(SwingConstants.RIGHT);
        display.setEditable(false);
        frame.add(display, BorderLayout.NORTH);

        // Buttons
        JPanel buttonPanel = new JPanel(new GridLayout(4, 4, 5, 5));

        String[] buttons = {
                "7", "8", "9", "/",
                "4", "5", "6", "*",
                "1", "2", "3", "-",
                "C", "0", "=", "+"
        };

        for (String text : buttons) {
            JButton button = new JButton(text);
            button.setFont(new Font("Arial", Font.BOLD, 18));
            button.addActionListener(new ButtonClickListener());
            buttonPanel.add(button);
        }

        frame.add(buttonPanel, BorderLayout.CENTER);
    }

    private class ButtonClickListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String command = e.getActionCommand();

            if ("0123456789".contains(command)) {
                currentInput.append(command);
                display.setText(currentInput.toString());
            } else if ("+-*/".contains(command)) {
                if (currentInput.length() > 0) {
                    firstOperand = Double.parseDouble(currentInput.toString());
                    currentInput.setLength(0);
                    operator = command;
                }
            } else if ("=".equals(command)) {
                if (currentInput.length() > 0 && !operator.isEmpty()) {
                    double secondOperand = Double.parseDouble(currentInput.toString());
                    double result = calculateResult(firstOperand, secondOperand, operator);
                    display.setText(String.valueOf(result));
                    currentInput.setLength(0);
                    operator = "";
                }
            } else if ("C".equals(command)) {
                currentInput.setLength(0);
                operator = "";
                firstOperand = 0;
                display.setText("");
            }
        }

        private double calculateResult(double firstOperand, double secondOperand, String operator) {
            switch (operator) {
                case "+": return firstOperand + secondOperand;
                case "-": return firstOperand - secondOperand;
                case "*": return firstOperand * secondOperand;
                case "/": return secondOperand != 0 ? firstOperand / secondOperand : Double.NaN;
                default: return 0;
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(SwingCalculator::new);
    }
}
