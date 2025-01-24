using System;
using System.Data.SQLite;

namespace UserManagementAppCSharp
{
    class Program
    {
        private const string ConnectionString = "Data Source=users.db;Version=3;";

        static void Main(string[] args)
        {
            // Tworzenie bazy danych
            CreateDatabase();

            int choice;
            do
            {
                Console.WriteLine("\n--- User Management System ---");
                Console.WriteLine("1. Add User");
                Console.WriteLine("2. View Users");
                Console.WriteLine("3. Update User");
                Console.WriteLine("4. Delete User");
                Console.WriteLine("5. Exit");
                Console.Write("Enter your choice: ");
                choice = int.Parse(Console.ReadLine());

                switch (choice)
                {
                    case 1:
                        AddUser();
                        break;
                    case 2:
                        ViewUsers();
                        break;
                    case 3:
                        UpdateUser();
                        break;
                    case 4:
                        DeleteUser();
                        break;
                    case 5:
                        Console.WriteLine("Exiting...");
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }
            } while (choice != 5);
        }

        private static void CreateDatabase()
        {
            using (var connection = new SQLiteConnection(ConnectionString))
            {
                connection.Open();
                string createTableSQL = @"
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        age INTEGER NOT NULL
                    );";
                using (var command = new SQLiteCommand(createTableSQL, connection))
                {
                    command.ExecuteNonQuery();
                }
                Console.WriteLine("Database and table created (if not already present).\n");
            }
        }

        private static void AddUser()
        {
            Console.Write("Enter first name: ");
            string firstName = Console.ReadLine();
            Console.Write("Enter last name: ");
            string lastName = Console.ReadLine();
            Console.Write("Enter age: ");
            int age = int.Parse(Console.ReadLine());

            using (var connection = new SQLiteConnection(ConnectionString))
            {
                connection.Open();
                string insertSQL = "INSERT INTO users (first_name, last_name, age) VALUES (@FirstName, @LastName, @Age);";
                using (var command = new SQLiteCommand(insertSQL, connection))
                {
                    command.Parameters.AddWithValue("@FirstName", firstName);
                    command.Parameters.AddWithValue("@LastName", lastName);
                    command.Parameters.AddWithValue("@Age", age);
                    command.ExecuteNonQuery();
                }
                Console.WriteLine("User added successfully!");
            }
        }

        private static void ViewUsers()
        {
            using (var connection = new SQLiteConnection(ConnectionString))
            {
                connection.Open();
                string selectSQL = "SELECT * FROM users;";
                using (var command = new SQLiteCommand(selectSQL, connection))
                {
                    using (var reader = command.ExecuteReader())
                    {
                        Console.WriteLine("\n--- User List ---");
                        while (reader.Read())
                        {
                            Console.WriteLine($"ID: {reader["id"]}, Name: {reader["first_name"]} {reader["last_name"]}, Age: {reader["age"]}");
                        }
                    }
                }
            }
        }

        private static void UpdateUser()
        {
            Console.Write("Enter user ID to update: ");
            int id = int.Parse(Console.ReadLine());

            using (var connection = new SQLiteConnection(ConnectionString))
            {
                connection.Open();

                // Pobierz dane użytkownika
                string selectSQL = "SELECT first_name, last_name, age FROM users WHERE id = @Id;";
                using (var command = new SQLiteCommand(selectSQL, connection))
                {
                    command.Parameters.AddWithValue("@Id", id);
                    using (var reader = command.ExecuteReader())
                    {
                        if (reader.Read())
                        {
                            // Pobierz obecne wartości
                            string currentFirstName = reader["first_name"].ToString();
                            string currentLastName = reader["last_name"].ToString();
                            int currentAge = int.Parse(reader["age"].ToString());

                            // Zapytaj użytkownika o każdą wartość
                            Console.Write($"First Name [{currentFirstName}]: ");
                            string newFirstName = Console.ReadLine();
                            if (string.IsNullOrEmpty(newFirstName)) newFirstName = currentFirstName;

                            Console.Write($"Last Name [{currentLastName}]: ");
                            string newLastName = Console.ReadLine();
                            if (string.IsNullOrEmpty(newLastName)) newLastName = currentLastName;

                            Console.Write($"Age [{currentAge}]: ");
                            string ageInput = Console.ReadLine();
                            int newAge = string.IsNullOrEmpty(ageInput) ? currentAge : int.Parse(ageInput);

                            // Aktualizacja danych
                            string updateSQL = "UPDATE users SET first_name = @FirstName, last_name = @LastName, age = @Age WHERE id = @Id;";
                            using (var updateCommand = new SQLiteCommand(updateSQL, connection))
                            {
                                updateCommand.Parameters.AddWithValue("@FirstName", newFirstName);
                                updateCommand.Parameters.AddWithValue("@LastName", newLastName);
                                updateCommand.Parameters.AddWithValue("@Age", newAge);
                                updateCommand.Parameters.AddWithValue("@Id", id);
                                int rowsAffected = updateCommand.ExecuteNonQuery();
                                Console.WriteLine(rowsAffected > 0 ? "User updated successfully!" : "Update failed.");
                            }
                        }
                        else
                        {
                            Console.WriteLine("User not found.");
                        }
                    }
                }
            }
        }

        private static void DeleteUser()
        {
            Console.Write("Enter user ID to delete: ");
            int id = int.Parse(Console.ReadLine());

            using (var connection = new SQLiteConnection(ConnectionString))
            {
                connection.Open();
                string deleteSQL = "DELETE FROM users WHERE id = @Id;";
                using (var command = new SQLiteCommand(deleteSQL, connection))
                {
                    command.Parameters.AddWithValue("@Id", id);
                    int rowsAffected = command.ExecuteNonQuery();
                    Console.WriteLine(rowsAffected > 0 ? "User deleted successfully!" : "User not found.");
                }
            }
        }
    }
}

