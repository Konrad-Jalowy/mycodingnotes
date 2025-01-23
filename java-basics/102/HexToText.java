public class HexToText {
    public static void main(String[] args) {
        String hex = "68 65 6C 6C 6F 20 77 6F 72 6C 64 21";
        String[] hexArray = hex.split(" ");
        StringBuilder result = new StringBuilder();

        for (String h : hexArray) {
            result.append((char) Integer.parseInt(h, 16));
        }

        System.out.println(result.toString()); // hello world!
    }
}