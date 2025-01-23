import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class BufferedWriterExample {
    public static void main(String[] args) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("example.txt"))) {
            writer.write("To jest zapis z buforowaniem.");
            writer.newLine(); // Dodaje nową linię
            writer.write("Dzięki buforowaniu zapis jest bardziej wydajny.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
