import java.net.Socket;
import java.io.OutputStream;
import java.io.InputStream;

public class SimpleSocketExample {
    public static void main(String[] args) throws Exception {
        try (Socket socket = new Socket("google.com", 80)) {
            OutputStream out = socket.getOutputStream();
            InputStream in = socket.getInputStream();

            String request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n";
            out.write(request.getBytes());
            out.flush();

            byte[] buffer = new byte[1024];
            int bytesRead = in.read(buffer);
            System.out.println(new String(buffer, 0, bytesRead));
        }
    }
}
