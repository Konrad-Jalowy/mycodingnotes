import java.io.InputStream;
import java.net.URL;

public class NetworkInputStreamExample {
    public static void main(String[] args) {
        try (InputStream inputStream = new URL("https://example.com").openStream()) {
            int data;
            while ((data = inputStream.read()) != -1) {
                System.out.print((char) data);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
