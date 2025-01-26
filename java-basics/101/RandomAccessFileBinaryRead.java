import java.io.RandomAccessFile;

public class RandomAccessFileBinaryRead {
    public static void main(String[] args) {
        try {
            RandomAccessFile file = new RandomAccessFile("example.bin", "r");

            // Odczyt bajtu
            int byteValue = file.read();
            System.out.println("Pierwszy bajt: " + byteValue);

            // Odczyt 4 bajtów jako liczba całkowita
            int intValue = file.readInt();
            System.out.println("Liczba całkowita: " + intValue);

            file.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
