import java.io.*;

public class BinaryExample {
    public static void main(String[] args) {
        String fileName = "data.bin";

        // Zapisujemy dane binarnie
        try (DataOutputStream dos = new DataOutputStream(new FileOutputStream(fileName))) {
            dos.writeInt(42); // Zapisz int (4 bajty)
            dos.writeDouble(3.14); // Zapisz double (8 bajtów)
            dos.writeUTF("Hello, world!"); // Zapisz UTF-8
            dos.writeUTF("Second string!"); // Drugi string
            System.out.println("Dane zapisane binarnie do pliku: " + fileName);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Odczytujemy dane binarnie
        try (DataInputStream dis = new DataInputStream(new FileInputStream(fileName))) {
            int number = dis.readInt(); // Odczytaj int
            double pi = dis.readDouble(); // Odczytaj double
            String firstString = dis.readUTF(); // Odczytaj pierwszy UTF
            String secondString = dis.readUTF(); // Odczytaj drugi UTF

            System.out.println("Odczytano dane:");
            System.out.println("Int: " + number);
            System.out.println("Double: " + pi);
            System.out.println("First String: " + firstString);
            System.out.println("Second String: " + secondString);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
