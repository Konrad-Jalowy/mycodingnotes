import java.io.*;
import java.nio.file.*;
import java.util.*;

public class FileSystemApp2 {

    public static void main(String[] args) {
        Path currentDirectory = Paths.get("").toAbsolutePath();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Witaj w prostym systemie plików!");
        System.out.println("Dostępne komendy: ls, cd, mkdir, rmdir, create, delete, read, write, help, exit\n");

        while (true) {
            System.out.print(currentDirectory + "> ");
            String input = scanner.nextLine().trim();

            if (input.isEmpty()) {
                continue;
            }

            String[] parts = input.split(" ", 2);
            String command = parts[0];
            String argument = parts.length > 1 ? parts[1] : "";
            List<String> flags = new ArrayList<>();

            if (!argument.isEmpty() && argument.contains(" ")) {
                String[] argParts = argument.split(" ");
                argument = argParts[0];
                for (int i = 1; i < argParts.length; i++) {
                    if (argParts[i].startsWith("-")) {
                        flags.add(argParts[i]);
                    }
                }
            }

            switch (command) {
                case "ls":
                    listDirectory(currentDirectory, argument, flags);
                    break;
                case "cd":
                    currentDirectory = changeDirectory(currentDirectory, argument);
                    break;
                case "mkdir":
                    createDirectory(currentDirectory, argument);
                    break;
                case "rmdir":
                    removeDirectory(currentDirectory, argument);
                    break;
                case "create":
                    createFile(currentDirectory, argument);
                    break;
                case "delete":
                    deleteFile(currentDirectory, argument);
                    break;
                case "read":
                    readFile(currentDirectory, argument, flags);
                    break;
                case "write":
                    writeToFile(currentDirectory, argument, scanner, flags);
                    break;
                case "help":
                    showHelp();
                    break;
                case "exit":
                    System.out.println("Do zobaczenia!");
                    return;
                default:
                    System.out.println("Nieznana komenda. Wpisz 'help', aby zobaczyć dostępne komendy.");
                    break;
            }
        }
    }

    private static void listDirectory(Path currentDirectory, String subDirectory, List<String> flags) {
        Path targetDirectory = subDirectory.isEmpty() ? currentDirectory : currentDirectory.resolve(subDirectory);

        if (!Files.exists(targetDirectory) || !Files.isDirectory(targetDirectory)) {
            System.out.println("Katalog nie istnieje lub nie jest katalogiem.");
            return;
        }

        System.out.println("\nZawartość katalogu:");
        try (DirectoryStream<Path> stream = Files.newDirectoryStream(targetDirectory)) {
            for (Path entry : stream) {
                if (flags.contains("-a")) {
                    File file = entry.toFile();
                    System.out.printf((Files.isDirectory(entry) ? "[DIR] " : "[FILE] ") + "%s (rozmiar: %d bajtów)%n",
                            entry.getFileName(), file.length());
                } else {
                    System.out.println((Files.isDirectory(entry) ? "[DIR] " : "[FILE] ") + entry.getFileName());
                }
            }
        } catch (IOException e) {
            System.out.println("Błąd podczas odczytu katalogu: " + e.getMessage());
        }
    }

    private static Path changeDirectory(Path currentDirectory, String newDir) {
        if (newDir.isEmpty()) {
            System.out.println("Podaj nazwę katalogu.");
            return currentDirectory;
        }

        Path targetDirectory = currentDirectory.resolve(newDir).normalize();
        if (Files.exists(targetDirectory) && Files.isDirectory(targetDirectory)) {
            return targetDirectory;
        } else {
            System.out.println("Katalog nie istnieje.");
            return currentDirectory;
        }
    }

    private static void createDirectory(Path currentDirectory, String dirName) {
        if (dirName.isEmpty()) {
            System.out.println("Podaj nazwę katalogu do utworzenia.");
            return;
        }

        Path newDirectory = currentDirectory.resolve(dirName);
        try {
            Files.createDirectory(newDirectory);
            System.out.println("Katalog utworzony: " + dirName);
        } catch (FileAlreadyExistsException e) {
            System.out.println("Katalog już istnieje.");
        } catch (IOException e) {
            System.out.println("Błąd tworzenia katalogu: " + e.getMessage());
        }
    }

    private static void removeDirectory(Path currentDirectory, String dirName) {
        if (dirName.isEmpty()) {
            System.out.println("Podaj nazwę katalogu do usunięcia.");
            return;
        }

        Path directoryToRemove = currentDirectory.resolve(dirName);
        try {
            Files.delete(directoryToRemove);
            System.out.println("Katalog usunięty: " + dirName);
        } catch (DirectoryNotEmptyException e) {
            System.out.println("Katalog nie jest pusty.");
        } catch (NoSuchFileException e) {
            System.out.println("Katalog nie istnieje.");
        } catch (IOException e) {
            System.out.println("Błąd usuwania katalogu: " + e.getMessage());
        }
    }

    private static void createFile(Path currentDirectory, String fileName) {
        if (fileName.isEmpty()) {
            System.out.println("Podaj nazwę pliku do utworzenia.");
            return;
        }

        Path newFile = currentDirectory.resolve(fileName);
        try {
            Files.createFile(newFile);
            System.out.println("Plik utworzony: " + fileName);
        } catch (FileAlreadyExistsException e) {
            System.out.println("Plik już istnieje.");
        } catch (IOException e) {
            System.out.println("Błąd tworzenia pliku: " + e.getMessage());
        }
    }

    private static void deleteFile(Path currentDirectory, String fileName) {
        if (fileName.isEmpty()) {
            System.out.println("Podaj nazwę pliku do usunięcia.");
            return;
        }

        Path fileToDelete = currentDirectory.resolve(fileName);
        try {
            Files.delete(fileToDelete);
            System.out.println("Plik usunięty: " + fileName);
        } catch (NoSuchFileException e) {
            System.out.println("Plik nie istnieje.");
        } catch (IOException e) {
            System.out.println("Błąd usuwania pliku: " + e.getMessage());
        }
    }

    private static void readFile(Path currentDirectory, String fileName, List<String> flags) {
        if (fileName.isEmpty()) {
            System.out.println("Podaj nazwę pliku do odczytu.");
            return;
        }

        Path fileToRead = currentDirectory.resolve(fileName);
        if (!Files.exists(fileToRead)) {
            System.out.println("Plik nie istnieje.");
            return;
        }

        try (BufferedReader reader = Files.newBufferedReader(fileToRead)) {
            String line;
            int lineNumber = 1;
            while ((line = reader.readLine()) != null) {
                if (flags.contains("-l")) {
                    System.out.printf("%d: %s%n", lineNumber++, line);
                } else {
                    System.out.println(line);
                }
            }
        } catch (IOException e) {
            System.out.println("Błąd odczytu pliku: " + e.getMessage());
        }
    }

    private static void writeToFile(Path currentDirectory, String fileName, Scanner scanner, List<String> flags) {
        if (fileName.isEmpty()) {
            System.out.println("Podaj nazwę pliku do zapisu.");
            return;
        }

        Path fileToWrite = currentDirectory.resolve(fileName);
        boolean append = !flags.contains("-w");
        System.out.println("Wprowadź dane do zapisania (zakończ wprowadzanie wpisując '\\0' w nowej linii):");
        try (BufferedWriter writer = Files.newBufferedWriter(fileToWrite,
                append ? StandardOpenOption.APPEND : StandardOpenOption.CREATE)) {
            while (true) {
                String line = scanner.nextLine();
                if ("\\0".equals(line)) {
                    break;
                }
                writer.write(line);
                writer.newLine();
            }
            System.out.println("Dane zapisane do pliku: " + fileName);
        } catch (IOException e) {
            System.out.println("Błąd zapisu do pliku: " + e.getMessage());
        }
    }

    private static void showHelp() {
        System.out.println("\nDostępne komendy:");
        System.out.println("ls [-a] - Wyświetl zawartość bieżącego katalogu");
        System.out.println("cd [nazwa] - Przejdź do innego katalogu");
        System.out.println("mkdir [nazwa] - Utwórz nowy katalog");
        System.out.println("rmdir [nazwa] - Usuń pusty katalog");
        System.out.println("create [nazwa] - Utwórz nowy plik");
        System.out.println("delete [nazwa] - Usuń plik");
        System.out.println("read [nazwa] [-l] - Odczytaj zawartość pliku z opcjonalnymi numerami linii");
        System.out.println("write [nazwa] [-w] - Dopisz dane do pliku lub nadpisz zawartość");
        System.out.println("help - Wyświetl pomoc");
        System.out.println("exit - Zakończ program\n");
    }
}
