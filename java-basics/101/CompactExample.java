import java.io.RandomAccessFile;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;

public class CompactExample {
    public static void main(String[] args) throws Exception {
        try (RandomAccessFile file = new RandomAccessFile("example.txt", "r");
             FileChannel channel = file.getChannel()) {

            ByteBuffer buffer = ByteBuffer.allocate(10);

            while (channel.read(buffer) != -1) {
                buffer.flip(); // Przełącz na tryb odczytu

                // Przetwarzamy część danych
                while (buffer.remaining() > 2) {
                    System.out.print((char) buffer.get());
                }

                // Zachowaj nieprzeczytane dane
                buffer.compact(); // Przesuń resztę danych na początek
            }

            buffer.flip(); // Odczyt ostatnich danych
            while (buffer.hasRemaining()) {
                System.out.print((char) buffer.get());
            }
        }
    }
}
