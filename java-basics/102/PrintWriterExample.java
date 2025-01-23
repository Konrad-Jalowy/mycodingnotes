import java.io.IOException;
import java.io.PrintWriter;
public class PrintWriterExample {
    public static void main(String[] args) {
        try (PrintWriter writer = new PrintWriter("example.txt")) {
            writer.println("Pierwsza linia tekstu.");
            writer.println("Druga linia tekstu.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
