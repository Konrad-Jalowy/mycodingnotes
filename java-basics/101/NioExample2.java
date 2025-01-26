import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.io.RandomAccessFile;

public class NioExample2 {
    public static void main(String[] args) throws Exception {
        // try-with-resources automatycznie zamyka zasoby
        try (RandomAccessFile file = new RandomAccessFile("example.txt", "rw");
             FileChannel channel = file.getChannel()) {

            ByteBuffer buffer = ByteBuffer.allocate(48);

            int bytesRead = channel.read(buffer);
            while (bytesRead != -1) {
                System.out.println("Bytes read: " + bytesRead);

                buffer.flip(); // Przełącz na tryb odczytu

                while (buffer.hasRemaining()) {
                    System.out.print((char) buffer.get());
                }

                buffer.clear(); // Przygotuj bufor na kolejne dane
                bytesRead = channel.read(buffer);
            }
        }
    }
}
