package 선택정렬;

class java {
    static void sel_sort(int[] arr){
        int len = arr.length;
        for(int i=0; i<len; i++){
            // 최솟값 구하기
            int min_inx = i;
            for(int j=i+1; j<len; j++){
                if(arr[j] < arr[min_inx]){
                    min_inx = j;
                }
            }
            // 최솟값과 맨 앞 값 바꾸기
            int temp = arr[min_inx];
            arr[min_inx] = arr[i];
            arr[i] = temp;
        }
    }
    public static void main(String[] args){
        int[] arr = new int[]{9, 4, 7, 1, 3};
        sel_sort(arr);
        for(int i : arr){
            System.out.print(i);
        }
    }
}
