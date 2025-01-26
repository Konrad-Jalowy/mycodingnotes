import java.io.RandomAccessFile;

public class RandomAccessFileAppend {
    public static void main(String[] args) {
        try {
            // Otwieramy plik w trybie odczytu i zapisu ("rw")
            RandomAccessFile file = new RandomAccessFile("example2.txt", "rw");

            file.seek(file.length()); // Przesuwamy wskaźnik na koniec
            file.writeBytes("Appending new data.\n");

            // Zamknięcie pliku
            file.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
