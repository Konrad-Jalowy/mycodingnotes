import java.io.RandomAccessFile;

public class RandomAccessFileModify {
    public static void main(String[] args) {
        try {
            // Otwórz plik w trybie odczytu i zapisu
            RandomAccessFile file = new RandomAccessFile("example.txt", "rw");

            // Przesuń wskaźnik zapisu/odczytu na 6. bajt
            file.seek(6);

            // Nadpisz dane od tej pozycji
            file.writeBytes("MODIFIED");

            // Zamknij plik
            file.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
