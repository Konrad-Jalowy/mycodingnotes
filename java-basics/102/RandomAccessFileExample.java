import java.io.RandomAccessFile;

public class RandomAccessFileExample {
    public static void main(String[] args) {
        try (RandomAccessFile file = new RandomAccessFile("example.txt", "rw")) {
            // Przejdź na początek pliku
            file.seek(0);
            System.out.println("Pierwszy znak: " + (char) file.read());

            // Przejdź na pozycję 10
            file.seek(10);
            System.out.println("Znak na pozycji 10: " + (char) file.read());

            // Dopisz tekst na końcu
            file.seek(file.length());
            file.write("Dopisano na końcu.".getBytes());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
