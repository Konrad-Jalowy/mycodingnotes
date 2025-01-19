import javax.swing.*;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Map;

public class UnitConverter6 {

    private static final Map<String, Double> UNIT_CONVERSIONS = Map.of(
            "Meters", 1.0,
            "Kilometers", 1000.0,
            "Miles", 1609.34,
            "Feet", 0.3048,
            "Kilograms", 1.0,
            "Grams", 0.001,
            "Pounds", 0.453592,
            "Celsius", 1.0,
            "Fahrenheit", 1.0,
            "Kelvin", 1.0
    );

    private static final Map<String, String> UNIT_CATEGORIES = Map.of(
            "Meters", "Length",
            "Kilometers", "Length",
            "Miles", "Length",
            "Feet", "Length",
            "Kilograms", "Mass",
            "Grams", "Mass",
            "Pounds", "Mass",
            "Celsius", "Temperature",
            "Fahrenheit", "Temperature",
            "Kelvin", "Temperature"
    );

    public static void main(String[] args) {
        SwingUtilities.invokeLater(UnitConverter6::createAndShowGUI);
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
        JComboBox<String> unitFromBox = new JComboBox<>(UNIT_CATEGORIES.keySet().toArray(new String[0]));

        JLabel unitToLabel = new JLabel("To Unit:");
        JComboBox<String> unitToBox = new JComboBox<>();

        // Ustaw domyślną zawartość unitToBox na podstawie pierwszego wyboru
        String defaultUnitFrom = (String) unitFromBox.getSelectedItem();
        updateUnitToBox(unitToBox, UNIT_CATEGORIES.get(defaultUnitFrom));

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

                        if (!UNIT_CATEGORIES.get(fromUnit).equals(UNIT_CATEGORIES.get(toUnit))) {
                            JOptionPane.showMessageDialog(frame, "Units are incompatible for conversion.", "Error", JOptionPane.ERROR_MESSAGE);
                            return;
                        }

                        double result;
                        if (UNIT_CATEGORIES.get(fromUnit).equals("Temperature")) {
                            result = convertTemperature(inputValue, fromUnit, toUnit);
                        } else {
                            result = convertUnits(inputValue, fromUnit, toUnit);
                        }

                        resultField.setText(String.format("%.2f", result));
                        inputField.setBorder(UIManager.getBorder("TextField.border"));
                    } catch (NumberFormatException ex) {
                        inputField.setBorder(BorderFactory.createLineBorder(Color.RED));
                        JOptionPane.showMessageDialog(frame, "Please enter a valid number.", "Input Error", JOptionPane.ERROR_MESSAGE);
                    }
                }
            }
        });

        unitFromBox.addActionListener(e -> {
            String selectedFromUnit = (String) unitFromBox.getSelectedItem();
            updateUnitToBox(unitToBox, UNIT_CATEGORIES.get(selectedFromUnit));
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
        double valueInBaseUnit = value * UNIT_CONVERSIONS.get(fromUnit);
        return valueInBaseUnit / UNIT_CONVERSIONS.get(toUnit);
    }

    private static double convertTemperature(double value, String fromUnit, String toUnit) {
        switch (fromUnit) {
            case "Celsius":
                if (toUnit.equals("Fahrenheit")) return value * 9/5 + 32;
                if (toUnit.equals("Kelvin")) return value + 273.15;
                break;
            case "Fahrenheit":
                if (toUnit.equals("Celsius")) return (value - 32) * 5/9;
                if (toUnit.equals("Kelvin")) return (value - 32) * 5/9 + 273.15;
                break;
            case "Kelvin":
                if (toUnit.equals("Celsius")) return value - 273.15;
                if (toUnit.equals("Fahrenheit")) return (value - 273.15) * 9/5 + 32;
                break;
        }
        throw new IllegalArgumentException("Invalid temperature conversion.");
    }

    private static void updateUnitToBox(JComboBox<String> unitToBox, String category) {
        unitToBox.removeAllItems();
        UNIT_CATEGORIES.forEach((unit, unitCategory) -> {
            if (unitCategory.equals(category)) {
                unitToBox.addItem(unit);
            }
        });
    }
}
