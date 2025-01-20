import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SwingCalculator3 {
    private JFrame frame;
    private JTextField display;
    private StringBuilder currentInput;
    private String operator;
    private double firstOperand;
    private boolean awaitingNextOperand;

    public SwingCalculator3() {
        frame = new JFrame("Kalkulator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 400);

        currentInput = new StringBuilder();
        operator = "";
        firstOperand = 0;
        awaitingNextOperand = false;

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
        JPanel buttonPanel = new JPanel(new GridLayout(5, 4, 5, 5));

        String[] buttons = {
                "7", "8", "9", "/",
                "4", "5", "6", "*",
                "1", "2", "3", "-",
                "C", "0", "<", "+",
                "+/-", "="
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
        private double lastResult;
        private String lastOperator;

        @Override
        public void actionPerformed(ActionEvent e) {
            String command = e.getActionCommand();

            if ("0123456789".contains(command)) {
                if (awaitingNextOperand) {
                    currentInput.setLength(0);
                    awaitingNextOperand = false;
                }
                currentInput.append(command);
                display.setText(currentInput.toString());
            } else if ("+-*/".contains(command)) {
                if (currentInput.length() > 0 || awaitingNextOperand) {
                    if (!operator.isEmpty() && !awaitingNextOperand) {
                        double secondOperand = Double.parseDouble(currentInput.toString());
                        firstOperand = calculateResult(firstOperand, secondOperand, operator);
                        display.setText(String.valueOf(firstOperand));
                    } else {
                        firstOperand = Double.parseDouble(currentInput.toString());
                    }
                    currentInput.setLength(0);
                    operator = command;
                    awaitingNextOperand = true;
                }
            } else if ("=".equals(command)) {
                if (!operator.isEmpty() && currentInput.length() > 0) {
                    double secondOperand = Double.parseDouble(currentInput.toString());
                    lastResult = calculateResult(firstOperand, secondOperand, operator);
                    display.setText(String.valueOf(lastResult));
                    firstOperand = lastResult;
                    lastOperator = operator;
                    operator = "";
                    awaitingNextOperand = true;
                } else if (!operator.isEmpty() && awaitingNextOperand) {
                    lastResult = calculateResult(firstOperand, firstOperand, operator);
                    display.setText(String.valueOf(lastResult));
                    firstOperand = lastResult;
                } else if (!Double.isNaN(lastResult) && lastOperator != null) {
                    lastResult = calculateResult(firstOperand, firstOperand, lastOperator);
                    display.setText(String.valueOf(lastResult));
                    firstOperand = lastResult;
                }
            } else if ("C".equals(command)) {
                currentInput.setLength(0);
                operator = "";
                firstOperand = 0;
                display.setText("");
                awaitingNextOperand = false;
            } else if ("<".equals(command)) {
                if (currentInput.length() > 0) {
                    currentInput.setLength(currentInput.length() - 1);
                    display.setText(currentInput.toString());
                }
            } else if ("+/-".equals(command)) {
                if (currentInput.length() > 0) {
                    if (currentInput.charAt(0) == '-') {
                        currentInput.deleteCharAt(0);
                    } else {
                        currentInput.insert(0, '-');
                    }
                    display.setText(currentInput.toString());
                }
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
        SwingUtilities.invokeLater(SwingCalculator3::new);
    }
}
