import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.io.RandomAccessFile;

public class EncodingExample {
    public static void main(String[] args) throws Exception {
        try (RandomAccessFile file = new RandomAccessFile("example.txt", "rw");
             FileChannel channel = file.getChannel()) {

            ByteBuffer buffer = ByteBuffer.allocate(48);

            int bytesRead = channel.read(buffer);
            while (bytesRead != -1) {
                buffer.flip();

                // Dekodowanie bajtów jako tekst UTF-8
                Charset charset = StandardCharsets.UTF_8;
                String text = charset.decode(buffer).toString();
                System.out.println(text);

                buffer.clear();
                bytesRead = channel.read(buffer);
            }
        }
    }
}
