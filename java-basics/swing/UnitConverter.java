import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class UnitConverter {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(UnitConverter::createAndShowGUI);
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
                try {
                    double inputValue = Double.parseDouble(inputField.getText());
                    String fromUnit = (String) unitFromBox.getSelectedItem();
                    String toUnit = (String) unitToBox.getSelectedItem();

                    double result = convertUnits(inputValue, fromUnit, toUnit);
                    resultField.setText(String.format("%.2f", result));
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "Please enter a valid number.", "Input Error", JOptionPane.ERROR_MESSAGE);
                }
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

    private static double convertUnits(double value, String fromUnit, String toUnit) {
        double valueInMeters = switch (fromUnit) {
            case "Meters" -> value;
            case "Kilometers" -> value * 1000;
            case "Miles" -> value * 1609.34;
            case "Feet" -> value * 0.3048;
            default -> throw new IllegalArgumentException("Invalid from unit");
        };

        return switch (toUnit) {
            case "Meters" -> valueInMeters;
            case "Kilometers" -> valueInMeters / 1000;
            case "Miles" -> valueInMeters / 1609.34;
            case "Feet" -> valueInMeters / 0.3048;
            default -> throw new IllegalArgumentException("Invalid to unit");
        };
    }
}
