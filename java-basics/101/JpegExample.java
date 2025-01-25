import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;
import javax.imageio.ImageWriteParam;
import javax.imageio.ImageWriter;
import javax.imageio.stream.ImageOutputStream;

public class JpegExample {
    public static void main(String[] args) {
        try {
            BufferedImage image = ImageIO.read(new File("example.png"));
            File compressedImageFile = new File("example_compressed.jpg");
            try (ImageOutputStream ios = ImageIO.createImageOutputStream(compressedImageFile)) {
                ImageWriter writer = ImageIO.getImageWritersByFormatName("jpg").next();
                writer.setOutput(ios);

                ImageWriteParam param = writer.getDefaultWriteParam();
                param.setCompressionMode(ImageWriteParam.MODE_EXPLICIT);
                param.setCompressionQuality(0.7f); // Jakość od 0.0 do 1.0

                writer.write(null, new javax.imageio.IIOImage(image, null, null), param);
                writer.dispose();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
