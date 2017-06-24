class ArrayStructure {

    public int[] array = new int[10];

    public void populate() {
        for(int i=0; i<10; ++i)
            array[i] = (int)(Math.random()*10)+10;
    }

    public void printArray() {
        for(int i: array)
            System.out.print(i+" ");
        System.out.println("\n");
    }

    public void swapValues(int pos1, int pos2) {
        int temp = array[pos1];
        array[pos1] = array[pos2];
        array[pos2] = temp;
    }

    public void bubbleSort() {
        for(int i=9; i>1; --i) {
            for(int j=0; j<i; ++j) {
                if(array[j] > array[j+1])
                    swapValues(j, j+1);
            printArray();
            }
        }
    }

    public void selectionSort() {
        printArray();
        for(int x = 0; x < 9; ++x) {
            // This considers that the minimum value in the array 
            // is stored in this index of the array
            int minimum = x;

            // To understand this, compile and run this method
            for(int y=x; y < 9; ++y) {
                // Found a smaller number than the guessed one,
                // then update the minimum variable with this value
                if(array[minimum] > array[y])
                    minimum = y;
            }

            swapValues(x, minimum);
            printArray();
        }
    }

    public void insertionSort() {
        for(int i=1; i<9; ++i) {
            int j = i;

            int toInsert = array[i];

            while ((j>0) && (array[j-1] > toInsert)) {
                array[j] = array[j-1];
                --j;
            }

            array[j] =  toInsert;
            printArray();
        }
    }

    public void binarySearch(int value) {
        // Indicates the start of the subarray that needs to be searched
        int lowIndex = 0;
        // Indicates the end of the subarray that needs to be searched
        int highIndex = 9;

        while(lowIndex <= highIndex) {
            // Gets the middle index of the subarray
            // In a sorted array comparing the search value to the value
            // at this index indicates in which portion of the array 
            // we need to look; greater than portion or less than portion
            int middleIndex = (highIndex + lowIndex) / 2;

            if(array[middleIndex] < value)
                lowIndex = middleIndex + 1 ;
            else if(array[middleIndex] > value)
                highIndex = middleIndex - 1;
            else {
                System.out.println("\nFound a match for "+value+" at "+middleIndex);
                return;
            }
        }
    }

    public static void main(String[] args) {
        ArrayStructure arr = new ArrayStructure();
        arr.populate();
        // arr.bubbleSort();
        // arr.selectionSort();
        arr.insertionSort();
    }
}

