import java.nio.ByteBuffer;

public class ByteBufferExample {
    public static void main(String[] args) {
        ByteBuffer buffer = ByteBuffer.allocate(10); // Tworzy bufor o pojemności 10 bajtów

        buffer.put((byte) 1);  // Zapisuje bajt
        buffer.put((byte) 2);  // Zapisuje bajt

        buffer.flip(); // Przełączenie na tryb odczytu

        while (buffer.hasRemaining()) {
            System.out.println(buffer.get()); // Odczyt danych
        }
    }
}
