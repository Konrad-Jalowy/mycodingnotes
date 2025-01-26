import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.Selector;
import java.nio.channels.SelectionKey;
import java.nio.channels.SocketChannel;
import java.util.Iterator;

public class NonBlockingSocketChannelExample3 {
    public static void main(String[] args) throws Exception {
        // Utwórz kanał i selektor w try-with-resources
        try (SocketChannel socketChannel = SocketChannel.open();
             Selector selector = Selector.open()) {

            socketChannel.configureBlocking(false); // Tryb nieblokujący
            socketChannel.connect(new InetSocketAddress("example.com", 80));
            socketChannel.register(selector, SelectionKey.OP_CONNECT);

            boolean displayedWaitingMessage = false;

            while (true) {
                // Czekaj na zdarzenia na kanałach
                selector.select();

                // Iteruj przez gotowe klucze
                Iterator<SelectionKey> keys = selector.selectedKeys().iterator();
                while (keys.hasNext()) {
                    SelectionKey key = keys.next();
                    keys.remove();

                    if (key.isConnectable()) {
                        SocketChannel channel = (SocketChannel) key.channel();
                        if (channel.finishConnect()) {
                            // Połączono z serwerem
                            System.out.println("\rPołączono z serwerem!");
                            System.out.flush(); // Wymuszenie wypisania
                            channel.register(selector, SelectionKey.OP_WRITE);
                        } else if (!displayedWaitingMessage) {
                            // Wyświetl jednorazowo komunikat oczekiwania
                            System.out.print("\rOczekiwanie na połączenie...");
                            System.out.flush(); // Wymuszenie wypisania
                            displayedWaitingMessage = true;
                        }
                    } else if (key.isWritable()) {
                        // Wyślij dane do serwera
                        SocketChannel channel = (SocketChannel) key.channel();
                        ByteBuffer buffer = ByteBuffer.wrap("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n".getBytes());
                        channel.write(buffer);
                        channel.register(selector, SelectionKey.OP_READ);
                    } else if (key.isReadable()) {
                        // Odczytaj dane od serwera
                        SocketChannel channel = (SocketChannel) key.channel();
                        ByteBuffer buffer = ByteBuffer.allocate(1024);
                        int bytesRead = channel.read(buffer);
                        if (bytesRead == -1) {
                            channel.close();
                            System.out.println("\nPołączenie zakończone.");
                            return;
                        }
                        buffer.flip();
                        while (buffer.hasRemaining()) {
                            System.out.print((char) buffer.get());
                        }
                    }
                }
            }
        }
    }
}
