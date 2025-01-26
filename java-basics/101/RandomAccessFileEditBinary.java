import java.io.RandomAccessFile;

public class RandomAccessFileEditBinary {
    public static void main(String[] args) {
        try {
            RandomAccessFile file = new RandomAccessFile("example.bin", "rw");

            // Przesunięcie do 8. bajtu
            file.seek(8);

            // Nadpisanie wartości
            file.writeInt(123456789); // Zapis liczby całkowitej

            file.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
