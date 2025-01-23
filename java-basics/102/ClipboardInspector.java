import java.awt.*;
import java.awt.datatransfer.*;
import java.io.IOException;

public class ClipboardInspector {

    public static void main(String[] args) {
        try {
            // Pobranie schowka systemowego
            Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();

            // Sprawdzenie, jakie dane są dostępne w schowku
            Transferable contents = clipboard.getContents(null);

            if (contents == null) {
                System.out.println("Schowek jest pusty.");
                return;
            }

            // Wyświetlenie typów danych w schowku
            DataFlavor[] dataFlavors = contents.getTransferDataFlavors();
            System.out.println("Dostępne typy danych w schowku:");
            for (DataFlavor flavor : dataFlavors) {
                System.out.println("- " + flavor.getHumanPresentableName());
            }

            // Sprawdzenie, czy w schowku jest tekst
            if (contents.isDataFlavorSupported(DataFlavor.stringFlavor)) {
                System.out.println("\nSchowek zawiera tekst:");
                // Odczytanie i wyświetlenie tekstu
                String text = (String) contents.getTransferData(DataFlavor.stringFlavor);
                System.out.println(text);
            } else {
                System.out.println("\nW schowku nie ma tekstu.");
            }

        } catch (UnsupportedFlavorException e) {
            System.err.println("Nieobsługiwany format danych w schowku.");
        } catch (IOException e) {
            System.err.println("Wystąpił błąd podczas odczytu danych ze schowka.");
        } catch (HeadlessException e) {
            System.err.println("Ten system nie obsługuje schowka.");
        }
    }
}
