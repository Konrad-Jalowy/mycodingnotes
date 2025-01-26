import java.nio.CharBuffer;

public class CharBufferExample {
    public static void main(String[] args) {
        CharBuffer buffer = CharBuffer.allocate(10); // Tworzy bufor o pojemności 10 znaków

        buffer.put("Hello"); // Zapisuje ciąg znaków
        buffer.flip();       // Przełączenie na tryb odczytu

        while (buffer.hasRemaining()) {
            System.out.print(buffer.get()); // Odczyt znaków
        }
    }
}
