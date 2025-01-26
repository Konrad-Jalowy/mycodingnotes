import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.Selector;
import java.nio.channels.SelectionKey;
import java.nio.channels.SocketChannel;
import java.util.Iterator;

public class ImprovedSocketChannelExample {
    public static void main(String[] args) throws Exception {
        try (SocketChannel socketChannel = SocketChannel.open();
             Selector selector = Selector.open()) {

            socketChannel.configureBlocking(false);
            socketChannel.connect(new InetSocketAddress("google.com", 80));
            socketChannel.register(selector, SelectionKey.OP_CONNECT);

            System.out.println("Oczekiwanie na połączenie...");

            while (true) {
                selector.select();

                Iterator<SelectionKey> keys = selector.selectedKeys().iterator();
                while (keys.hasNext()) {
                    SelectionKey key = keys.next();
                    keys.remove();

                    if (key.isConnectable()) {
                        SocketChannel channel = (SocketChannel) key.channel();
                        if (channel.finishConnect()) {
                            System.out.println("Połączono z serwerem!");
                            channel.register(selector, SelectionKey.OP_WRITE);
                        }
                    } else if (key.isWritable()) {
                        SocketChannel channel = (SocketChannel) key.channel();
                        ByteBuffer buffer = ByteBuffer.wrap("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".getBytes());
                        channel.write(buffer);
                        channel.register(selector, SelectionKey.OP_READ);
                    } else if (key.isReadable()) {
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
}
