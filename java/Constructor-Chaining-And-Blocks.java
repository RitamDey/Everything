class Flight {
	private int passengers, flightNumber, seats;
	private char flightClass;
	private boolean[] isSeatAvaliable;

	{
		// This is an initialization block. This run automatically
		// during the object creation of this class. Also multiple
		// blocks can be avaliable in a class and those will be
		// executed in the order they are encountered
		isSeatAvaliable = new boolean[seats];

		for(int i=0; i < seats; ++i)
			isSeatAvaliable[i] = false;
	}

	public Flight() { this.seats = 150; }

	public Flight(int flightNumber) {
		this.flightNumber = flightNumber;
	}

	public Flight(char flightClass) {
		this.flightClass = flightClass;
	}
}


class Driver {
	public static void main(String[] args) {
		Flight f1 = new Flight(150);
		Flight f2 = new Flight('S');
	}
}
