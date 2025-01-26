import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.Selector;
import java.nio.channels.SelectionKey;
import java.nio.channels.SocketChannel;
import java.util.Iterator;

public class NonBlockingSocketChannelExample {
    public static void main(String[] args) throws Exception {
        // Utwórz kanał
        SocketChannel socketChannel = SocketChannel.open();
        socketChannel.configureBlocking(false); // Ustaw tryb nieblokujący

        // Połącz z serwerem
        socketChannel.connect(new InetSocketAddress("example.com", 80));

        // Utwórz selektor
        Selector selector = Selector.open();
        socketChannel.register(selector, SelectionKey.OP_CONNECT);

        while (true) {
            // Czekaj na zdarzenia na kanałach
            selector.select();

            // Iteruj przez gotowe klucze
            Iterator<SelectionKey> keys = selector.selectedKeys().iterator();
            while (keys.hasNext()) {
                SelectionKey key = keys.next();
                keys.remove();

                if (key.isConnectable()) {
                    // Zakończ łączenie
                    SocketChannel channel = (SocketChannel) key.channel();
                    if (channel.finishConnect()) {
                        System.out.println("Połączono z serwerem");
                        channel.register(selector, SelectionKey.OP_WRITE);
                    }
                } else if (key.isWritable()) {
                    // Wyślij dane
                    SocketChannel channel = (SocketChannel) key.channel();
                    ByteBuffer buffer = ByteBuffer.wrap("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n".getBytes());
                    channel.write(buffer);
                    channel.register(selector, SelectionKey.OP_READ); // Zmień na odczyt
                } else if (key.isReadable()) {
                    // Odczytaj dane
                    SocketChannel channel = (SocketChannel) key.channel();
                    ByteBuffer buffer = ByteBuffer.allocate(1024);
                    int bytesRead = channel.read(buffer);
                    if (bytesRead == -1) {
                        channel.close();
                        System.out.println("Połączenie zakończone.");
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
