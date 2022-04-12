package 삽입정렬;

public class java {
    static void inseration_sort(int[] arr){
        int len = arr.length;
        for(int i=1; i<len; i++){
            int key = arr[i];
            int j = i-1;
            while(j>=0 && arr[j]>key){
                arr[j+1] = arr[j];
                j -= 1;
            }
            arr[j+1] = key;
        }
    }
    public static void main(String[] args){
        int[] arr = new int[]{1,5,6,2,3};
        inseration_sort(arr);
        for(int i : arr){
            System.out.print(i);
        } 
    }
    
}
