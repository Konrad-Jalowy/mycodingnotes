import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.io.RandomAccessFile;

public class NioExample {
    public static void main(String[] args) throws Exception {
        // Otwórz plik za pomocą FileChannel
        RandomAccessFile file = new RandomAccessFile("example.txt", "rw");
        FileChannel channel = file.getChannel();

        // Utwórz bufor
        ByteBuffer buffer = ByteBuffer.allocate(48);

        // Odczyt z kanału do bufora
        int bytesRead = channel.read(buffer);
        while (bytesRead != -1) {
            System.out.println("Bytes read: " + bytesRead);

            // Przełączenie bufora na tryb odczytu
            buffer.flip();

            while (buffer.hasRemaining()) {
                System.out.print((char) buffer.get());
            }

            // Wyczyść bufor, by móc ponownie pisać
            buffer.clear();
            bytesRead = channel.read(buffer);
        }
        file.close();
    }
}
