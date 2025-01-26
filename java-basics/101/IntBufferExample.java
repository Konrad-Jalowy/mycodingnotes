import java.nio.IntBuffer;

public class IntBufferExample {
    public static void main(String[] args) {
        IntBuffer buffer = IntBuffer.allocate(5); // Tworzy bufor o pojemności 5 liczb całkowitych

        buffer.put(10); // Zapisuje liczbę całkowitą
        buffer.put(20);
        buffer.put(30);

        buffer.flip(); // Przełączenie na tryb odczytu

        while (buffer.hasRemaining()) {
            System.out.println(buffer.get()); // Odczyt liczb całkowitych
        }
    }
}
