import java.io.RandomAccessFile;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;

public class MappedByteBufferExample {
    public static void main(String[] args) throws Exception {
        try (RandomAccessFile file = new RandomAccessFile("example.txt", "rw");
             FileChannel channel = file.getChannel()) {

            // Mapowanie pierwszych 100 bajtów pliku na pamięć
            MappedByteBuffer buffer = channel.map(FileChannel.MapMode.READ_WRITE, 0, 100);

            // Odczyt danych
            while (buffer.hasRemaining()) {
                System.out.print((char) buffer.get());
            }

            // Modyfikacja danych
            buffer.put(0, (byte) 'H'); // Zmiana pierwszego bajtu na 'H'

            System.out.println("\nDane w pliku zostały zmodyfikowane.");
        }
    }
}
