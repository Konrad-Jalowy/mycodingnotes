import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.Selector;
import java.nio.channels.SelectionKey;
import java.nio.channels.SocketChannel;
import java.util.Iterator;

public class NonBlockingSocketChannelExample4 {
    public static void main(String[] args) throws Exception {
        try (Selector selector = Selector.open();
             SocketChannel socketChannel = SocketChannel.open()) {

            socketChannel.configureBlocking(false);
            socketChannel.connect(new InetSocketAddress("example.com", 80));
            socketChannel.register(selector, SelectionKey.OP_CONNECT);

            while (true) {
                selector.select();

                Iterator<SelectionKey> keys = selector.selectedKeys().iterator();
                while (keys.hasNext()) {
                    SelectionKey key = keys.next();
                    keys.remove();

                    try {
                        if (key.isConnectable()) {
                            handleConnect(key);
                        } else if (key.isWritable()) {
                            handleWrite(key);
                        } else if (key.isReadable()) {
                            handleRead(key);
                        }
                    } catch (Exception e) {
                        key.channel().close(); // Zamknij kanał w przypadku błędu
                        key.cancel();
                    }
                }
            }
        }
    }

    private static void handleConnect(SelectionKey key) throws Exception {
        SocketChannel channel = (SocketChannel) key.channel();
        if (channel.finishConnect()) {
            System.out.println("\rPołączono z serwerem!");
            channel.register(key.selector(), SelectionKey.OP_WRITE);
        }
    }

    private static void handleWrite(SelectionKey key) throws Exception {
        SocketChannel channel = (SocketChannel) key.channel();
        ByteBuffer buffer = ByteBuffer.wrap("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n".getBytes());
        channel.write(buffer);
        channel.register(key.selector(), SelectionKey.OP_READ);
    }

    private static void handleRead(SelectionKey key) throws Exception {
        SocketChannel channel = (SocketChannel) key.channel();
        ByteBuffer buffer = ByteBuffer.allocate(1024);
        int bytesRead = channel.read(buffer);

        if (bytesRead == -1) {
            // Zamknij kanał, jeśli serwer zakończy połączenie
            channel.close();
            key.cancel();
            System.out.println("Połączenie zakończone.");
            return;
        }

        buffer.flip();
        while (buffer.hasRemaining()) {
            System.out.print((char) buffer.get());
        }
    }
}
