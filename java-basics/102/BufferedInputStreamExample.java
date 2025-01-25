import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.InputStream;

public class BufferedInputStreamExample {
    public static void main(String[] args) {
        try (InputStream inputStream = new BufferedInputStream(new FileInputStream("example.txt"))) {
            int data;
            while ((data = inputStream.read()) != -1) {
                System.out.print((char) data);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}