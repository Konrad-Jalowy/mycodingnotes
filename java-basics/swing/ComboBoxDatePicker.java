import javax.swing.*;
import java.awt.*;
import java.time.LocalDate;
import java.time.YearMonth;
import java.util.Calendar;

public class ComboBoxDatePicker {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Custom Date Picker");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);
        frame.setLayout(new FlowLayout());

        // Day combo box
        JComboBox<Integer> dayBox = new JComboBox<>();
        for (int i = 1; i <= 31; i++) {
            dayBox.addItem(i);
        }

        // Month combo box
        JComboBox<String> monthBox = new JComboBox<>(new String[]{
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
        });

        // Year combo box
        JComboBox<Integer> yearBox = new JComboBox<>();
        int currentYear = Calendar.getInstance().get(Calendar.YEAR);
        for (int i = currentYear - 100; i <= currentYear + 50; i++) {
            yearBox.addItem(i);
        }

        // Update the number of days when the year or month changes
        Runnable updateDays = () -> {
            int year = (int) yearBox.getSelectedItem();
            int month = monthBox.getSelectedIndex() + 1; // Months are 0-based in ComboBox

            // Get the number of days in the selected month/year
            int daysInMonth = YearMonth.of(year, month).lengthOfMonth();

            // Update the day combo box
            dayBox.removeAllItems();
            for (int i = 1; i <= daysInMonth; i++) {
                dayBox.addItem(i);
            }
        };

        yearBox.addActionListener(e -> updateDays.run());
        monthBox.addActionListener(e -> updateDays.run());

        // Set initial state
        updateDays.run();

        // Add components to frame
        frame.add(new JLabel("Day:"));
        frame.add(dayBox);
        frame.add(new JLabel("Month:"));
        frame.add(monthBox);
        frame.add(new JLabel("Year:"));
        frame.add(yearBox);

        frame.setVisible(true);
    }
}
