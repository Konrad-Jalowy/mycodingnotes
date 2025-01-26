import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.SocketChannel;

public class SocketChannelExample {
    public static void main(String[] args) throws Exception {
        try (SocketChannel socketChannel = SocketChannel.open(new InetSocketAddress("example.com", 80))) {
            socketChannel.configureBlocking(true);

            // Wysyłanie zapytania HTTP
            String request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n";
            ByteBuffer buffer = ByteBuffer.wrap(request.getBytes());
            socketChannel.write(buffer);

            // Odczyt odpowiedzi
            buffer.clear();
            socketChannel.read(buffer);
            buffer.flip();
            while (buffer.hasRemaining()) {
                System.out.print((char) buffer.get());
            }
        }
    }
}
