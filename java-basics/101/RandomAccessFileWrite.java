import java.io.RandomAccessFile;

public class RandomAccessFileWrite {
    public static void main(String[] args) {
        try {
            // Otwieramy plik w trybie odczytu i zapisu ("rw")
            RandomAccessFile file = new RandomAccessFile("example2.txt", "rw");

            // Zapisujemy dane na początku pliku
            file.writeBytes("Hello, world!\n");
            file.writeBytes("This is a new line.\n");

            // Zamknięcie pliku
            file.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
