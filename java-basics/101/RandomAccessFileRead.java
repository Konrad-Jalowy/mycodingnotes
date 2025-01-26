import java.io.RandomAccessFile;

public class RandomAccessFileRead {
    public static void main(String[] args) {
        try {
            // Otwieramy plik w trybie odczytu ("r")
            RandomAccessFile file = new RandomAccessFile("example.txt", "r");

            // Odczyt linii z pliku
            String line = file.readLine();
            while (line != null) {
                System.out.println(line);
                line = file.readLine(); // Odczyt kolejnej linii
            }

            // Zamknięcie pliku
            file.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
