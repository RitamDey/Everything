import java.util.Arrays;


class HashFunction {
    String[] array;
    int size;
    int items = 0;


    public void hash1(String[] stringsForArray, String[] thearr) {
        // Very simple hash function
        for(int n=0; n<stringsForArray.length; ++n) {
            String newElement = stringsForArray[n];

            thearr[Integer.parseInt(newElement)] = newElement;
        }
    }


    public void hash2(String[] stringsForArray, String[] thearr) {
        for(int n=0; n<stringsForArray.length; ++n) {
            String newElementVal = stringsForArray[n];

            int arrayIndex = Integer.parseInt(newElementVal) % 29;
            System.out.println("Modulus Index="+arrayIndex);

            while(thearr[arrayIndex] != "-1") {
                ++arrayIndex;
                System.out.println("Collision. Index="+arrayIndex);
                arrayIndex %= this.size;
            }

            thearr[arrayIndex] = newElementVal;
        }
    }


    public String findKey(String key) {
        int arrayIndexHash = Integer.parseInt(key) % 29;

        while(this.array[arrayIndexHash] != "-1") {
            if(this.array[arrayIndexHash] == key) {
                System.out.println(key+" was found in index "+arrayIndexHash);
            
                return this.array[arrayIndexHash];
            }

            ++arrayIndexHash;

            arrayIndexHash %= this.size;
        }

        return null;
    }


    public static void main(String[] args) {
        HashFunction func = new HashFunction(30);

        // String[] elementsToAdd = {"1", "5", "17", "21", "26"};
        // func.hash1(elementsToAdd, func.array);

        String[] elementsToAdd2 = { "100", "510", "170", "214", "268", "398",
				"235", "802", "900", "723", "699", "1", "16", "999", "890",
				"725", "998", "978", "988", "990", "989", "984", "320", "321",
				"400", "415", "450", "50", "660", "624" };
        
        func.hash2(elementsToAdd2, func.array);
        func.displayTheStack();

        func.findKey("660");
    }


    HashFunction(int size) {
        this.size = size;
        this.array = new String[size];
        Arrays.fill(this.array, "-1");
    }


    public void displayTheStack() {
		int increment = 0;

		for (int m = 0; m < 3; m++) {
			increment += 10;

			for (int n = 0; n < 71; n++)
				System.out.print("-");

			System.out.println();
			for (int n = increment - 10; n < increment; n++)
				System.out.format("| %3s " + " ", n);

			System.out.println("|");
			for (int n = 0; n < 71; n++)
				System.out.print("-");

			System.out.println();
			for (int n = increment - 10; n < increment; n++) {
				if (array   [n].equals("-1"))
					System.out.print("|      ");
				else
					System.out.print(String.format("| %3s " + " ", array    [n]));

			}
			System.out.println("|");
			for (int n = 0; n < 71; n++)
				System.out.print("-");

			System.out.println();

		}

	}

}