package 버블정렬;
import java.util.Arrays;

public class java {
    static void bubble_sort(int[] arr){
        int len = arr.length;
        for(int i=0; i<len; i++){
            for(int j=0; j<len-i-1; j++){
                if(arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
            System.out.println(i+1 + "번째 : " + Arrays.toString(arr));
        }
    }
    public static void main(String[] args){
        int[] arr = new int[]{4,6,2,1,3};
        bubble_sort(arr);
        System.out.println("결과 : " + Arrays.toString(arr));
    }
}
