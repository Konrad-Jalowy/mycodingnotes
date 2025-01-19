import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class UserManagementApp {
    private JFrame frame;
    private JTable table;
    private DefaultTableModel tableModel;

    public UserManagementApp() {
        // Frame setup
        frame = new JFrame("User Management App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);

        // Table setup
        String[] columnNames = {"Name", "Age"};
        tableModel = new DefaultTableModel(columnNames, 0);
        table = new JTable(tableModel);
        JScrollPane scrollPane = new JScrollPane(table);

        // Buttons
        JButton addButton = new JButton("Add User");
        JButton editButton = new JButton("Edit User");
        JButton deleteButton = new JButton("Delete User");

        // Button panel
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(addButton);
        buttonPanel.add(editButton);
        buttonPanel.add(deleteButton);

        // Layout
        frame.setLayout(new BorderLayout());
        frame.add(scrollPane, BorderLayout.CENTER);
        frame.add(buttonPanel, BorderLayout.SOUTH);

        // Button actions
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addUser();
            }
        });

        editButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                editUser();
            }
        });

        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                deleteUser();
            }
        });

        // Show frame
        frame.setVisible(true);
    }

    private void addUser() {
        String name = JOptionPane.showInputDialog(frame, "Enter name:");
        if (name == null || name.trim().isEmpty()) {
            return; // Cancel or invalid input
        }

        String ageStr = JOptionPane.showInputDialog(frame, "Enter age:");
        if (ageStr == null || !ageStr.matches("\\d+")) {
            JOptionPane.showMessageDialog(frame, "Invalid age!", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        int age = Integer.parseInt(ageStr);
        tableModel.addRow(new Object[]{name, age});
    }

    private void editUser() {
        int selectedRow = table.getSelectedRow();
        if (selectedRow == -1) {
            JOptionPane.showMessageDialog(frame, "No user selected!", "Warning", JOptionPane.WARNING_MESSAGE);
            return;
        }

        String name = (String) tableModel.getValueAt(selectedRow, 0);
        int age = (int) tableModel.getValueAt(selectedRow, 1);

        String newName = JOptionPane.showInputDialog(frame, "Edit name:", name);
        if (newName == null || newName.trim().isEmpty()) {
            return; // Cancel or invalid input
        }

        String newAgeStr = JOptionPane.showInputDialog(frame, "Edit age:", age);
        if (newAgeStr == null || !newAgeStr.matches("\\d+")) {
            JOptionPane.showMessageDialog(frame, "Invalid age!", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        int newAge = Integer.parseInt(newAgeStr);
        tableModel.setValueAt(newName, selectedRow, 0);
        tableModel.setValueAt(newAge, selectedRow, 1);
    }

    private void deleteUser() {
        int selectedRow = table.getSelectedRow();
        if (selectedRow == -1) {
            JOptionPane.showMessageDialog(frame, "No user selected!", "Warning", JOptionPane.WARNING_MESSAGE);
            return;
        }

        tableModel.removeRow(selectedRow);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(UserManagementApp::new);
    }
}
