import java.io.*;

public class CustomEncodingWriteExample {
    public static void main(String[] args) {
        try (OutputStreamWriter writer = new OutputStreamWriter(new FileOutputStream("example.txt"), "UTF-8")) {
            writer.write("To jest zapis z kodowaniem UTF-8.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
