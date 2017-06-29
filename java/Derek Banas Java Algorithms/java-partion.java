import java.util.Arrays;


class Partitioning {
    private static int[] array;
    private static int size;


    public static void main(String[] args) {
        Partitioning partion = new Partitioning(10);
        System.out.println(Arrays.toString(partion.array));

        partion.partition(35);
        System.out.println(Arrays.toString(partion.array));
    }


    public void partition(int pivot) {
        int left = -1;
        int right = size;

        while(true){
            while(left < (this.size -1) && this.array[++left] < pivot);
            System.out.println("Bigger value found against pivot "+pivot+" is "+this.array[left]);
            while(right > 0 && this.array[--right] > pivot);
            System.out.println("Smaller value found against pivot "+pivot+" is "+this.array[right]);

            if(left >= right) break;

            else {
                this.swap(left, right);
                System.out.println(this.array[left]+" was swapped for "+this.array[right]);
            }

        }
    }


    public void swap(int pos1, int pos2) {
        int temp = this.array[pos1];
        this.array[pos1] = this.array[pos2];
        this.array[pos2] = temp;
    }


    public void generate() {
        for(int i=0; i<this.size; ++i)
            this.array[i] = (int)(Math.random()*50)+10;
    }


    Partitioning(int size) {
        this.size = size;
        this.array = new int[size];
        this.generate();
    }
}


class QuickSort {
    
}