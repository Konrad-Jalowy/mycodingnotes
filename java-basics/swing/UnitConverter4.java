import javax.swing.*;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Map;

public class UnitConverter4 {

    private static final Map<String, Double> UNIT_CONVERSIONS = Map.of(
            "Meters", 1.0,
            "Kilometers", 1000.0,
            "Miles", 1609.34,
            "Feet", 0.3048
    );

    public static void main(String[] args) {
        SwingUtilities.invokeLater(UnitConverter4::createAndShowGUI);
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Unit Converter");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(4, 2, 10, 10));

        JLabel inputLabel = new JLabel("Input Value:");
        JTextField inputField = new JTextField();

        JLabel unitFromLabel = new JLabel("From Unit:");
        JComboBox<String> unitFromBox = new JComboBox<>(new String[]{"Meters", "Kilometers", "Miles", "Feet"});

        JLabel unitToLabel = new JLabel("To Unit:");
        JComboBox<String> unitToBox = new JComboBox<>(new String[]{"Meters", "Kilometers", "Miles", "Feet"});

        JLabel resultLabel = new JLabel("Result:");
        JTextField resultField = new JTextField();
        resultField.setEditable(false);

        JButton convertButton = new JButton("Convert");
        convertButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (validateInput(inputField)) {
                    try {
                        double inputValue = Double.parseDouble(inputField.getText());
                        String fromUnit = (String) unitFromBox.getSelectedItem();
                        String toUnit = (String) unitToBox.getSelectedItem();

                        if (fromUnit.equals(toUnit)) {
                            JOptionPane.showMessageDialog(frame, "The selected units are the same. No conversion is needed.", "Info", JOptionPane.INFORMATION_MESSAGE);
                            resultField.setText(String.format("%.2f", inputValue));
                            return;
                        }

                        double result = convertUnits(inputValue, fromUnit, toUnit);
                        resultField.setText(String.format("%.2f", result));
                        inputField.setBorder(UIManager.getBorder("TextField.border"));
                    } catch (NumberFormatException ex) {
                        inputField.setBorder(BorderFactory.createLineBorder(Color.RED));
                        JOptionPane.showMessageDialog(frame, "Please enter a valid number.", "Input Error", JOptionPane.ERROR_MESSAGE);
                    }
                }
            }
        });

        inputField.getDocument().addDocumentListener(new DocumentListener() {
            @Override
            public void insertUpdate(DocumentEvent e) {
                validateInput(inputField);
            }

            @Override
            public void removeUpdate(DocumentEvent e) {
                validateInput(inputField);
            }

            @Override
            public void changedUpdate(DocumentEvent e) {
                validateInput(inputField);
            }
        });

        panel.add(inputLabel);
        panel.add(inputField);
        panel.add(unitFromLabel);
        panel.add(unitFromBox);
        panel.add(unitToLabel);
        panel.add(unitToBox);
        panel.add(resultLabel);
        panel.add(resultField);

        frame.add(panel, BorderLayout.CENTER);
        frame.add(convertButton, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private static boolean validateInput(JTextField inputField) {
        String text = inputField.getText();
        try {
            Double.parseDouble(text);
            inputField.setBorder(UIManager.getBorder("TextField.border"));
            return true;
        } catch (NumberFormatException e) {
            if (!text.isEmpty()) {
                inputField.setBorder(BorderFactory.createLineBorder(Color.RED));
            } else {
                inputField.setBorder(UIManager.getBorder("TextField.border"));
            }
            return false;
        }
    }

    private static double convertUnits(double value, String fromUnit, String toUnit) {
        if (!UNIT_CONVERSIONS.containsKey(fromUnit) || !UNIT_CONVERSIONS.containsKey(toUnit)) {
            throw new IllegalArgumentException("Invalid unit");
        }

        double valueInMeters = value * UNIT_CONVERSIONS.get(fromUnit);
        return valueInMeters / UNIT_CONVERSIONS.get(toUnit);
    }
}
