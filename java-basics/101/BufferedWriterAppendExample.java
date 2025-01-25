import java.io.*;

public class BufferedWriterAppendExample {
    public static void main(String[] args) {
        try (BufferedWriter bw = new BufferedWriter(
                new OutputStreamWriter(
                        new FileOutputStream("example.txt", true), // true = append
                        "UTF-8" // Kodowanie
                ))) {
            bw.write("Dopisany tekst w UTF-8."); // Dopisujemy tekst
            bw.newLine(); // Dodajemy nową linię (System.lineSeparator())
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
