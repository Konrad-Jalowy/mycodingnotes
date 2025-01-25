import java.io.*;
import java.nio.charset.StandardCharsets;

public class BufferedWriterAppendExample2 {
    public static void main(String[] args) {
        try (BufferedWriter bw = new BufferedWriter(
                new OutputStreamWriter(
                        new FileOutputStream("example.txt", true), // true = append
                        StandardCharsets.UTF_8 // Kodowanie
                ))) {
            bw.write("Dopisany tekst w UTF-8."); // Dopisujemy tekst
            bw.newLine(); // Dodajemy nową linię (System.lineSeparator())
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
