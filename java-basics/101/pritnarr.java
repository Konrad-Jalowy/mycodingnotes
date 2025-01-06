public class Main {
    public static void main(String[] args) {
        int mynums[] = {1,2,3,4,5};
        printArray(mynums);
    }
    public static void printArray(int []array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]+"  ");
        }
    }
}