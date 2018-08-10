// Method only submission
//
class Printable <T> {
	public <T> void printArray(T[] arr) {
		for (T elem: arr)
			System.out.println(elem.toString());
	}
}

