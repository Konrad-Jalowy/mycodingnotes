import java.awt.*;
import java.awt.datatransfer.*;
import java.io.IOException;

public class ClipboardInspectorDetailed {

    public static void main(String[] args) {
        try {
            Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
            Transferable contents = clipboard.getContents(null);

            if (contents == null) {
                System.out.println("Schowek jest pusty.");
                return;
            }

            DataFlavor[] flavors = contents.getTransferDataFlavors();
            System.out.println("Dostępne typy danych w schowku:");
            for (DataFlavor flavor : flavors) {
                System.out.println("- " + flavor.getHumanPresentableName());
                try {
                    Object data = contents.getTransferData(flavor);
                    System.out.println("  Zawartość: " + data);
                } catch (Exception e) {
                    System.out.println("  Nie można odczytać danych dla tego formatu.");
                }
            }

        } catch (HeadlessException e) {
            System.err.println("System nie obsługuje schowka.");
        }
    }
}