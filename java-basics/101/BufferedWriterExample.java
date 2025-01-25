import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;

public class BufferedWriterExample {
    public static void main(String[] args) {
        String data = "Wydajny zapis z buforowaniem.";
        try (BufferedWriter bufferedWriter = new BufferedWriter(
                new OutputStreamWriter(new FileOutputStream("buffered_output.txt"), "UTF-8"))) {

            bufferedWriter.write(data);
            bufferedWriter.newLine(); // Dodanie nowej linii
            bufferedWriter.write("Druga linia tekstu.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
