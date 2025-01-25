import java.io.*;

public class DataStreamExample {
    public static void main(String[] args) {
        String fileName = "data.bin";

        // Zapis danych do pliku binarnego
        try (DataOutputStream dos = new DataOutputStream(new FileOutputStream(fileName))) {
            dos.writeInt(42);
            dos.writeDouble(3.14);
            dos.writeUTF("Hello, world!");
            System.out.println("Dane zapisane.");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Odczyt danych z pliku binarnego
        try (DataInputStream dis = new DataInputStream(new FileInputStream(fileName))) {
            int number = dis.readInt();
            double pi = dis.readDouble();
            String text = dis.readUTF();

            System.out.println("Odczytano: " + number + ", " + pi + ", " + text);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}