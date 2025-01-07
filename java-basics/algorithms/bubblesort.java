public class Main {
    public static void main(String[] args) {
        int[] myNums = {5,3,4,71,2};
        printArray(myNums);
        bubbleSort(myNums);
        System.out.println();
        printArray(myNums);
    }
    public static void bubbleSort(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            for (int j =0; j < n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
    public static void printArray(int []array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]+"  ");
        }
    }
}