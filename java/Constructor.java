class Flight {
	int seats;
	int booked_seats;

	Flight() {
		seats = 70;
		booked_seats = 0;
	}

	Flight(int custom) {
		seats = custom;
		booked_seats = 0;
	}

	public int filled_status() {
		return this.booked_seats;
	}

	public boolean book() {
		if(this.booked_seats == this.seats)
			return false;

		this.booked_seats++;
		return true;
	}

	public boolean book(int count) {
		booked_seats += count;

		if(booked_seats > seats) {
			booked_seats -= count;
			return false;
		}

		return true;
	}
}


class Constructor {
	public static void main(String[] args) {
		Flight f1 = new Flight();
		Flight f2 = new Flight(100);

		System.out.println(f1.book());
		System.out.println(f1.book());
		System.out.println(f1.book(50));
		System.out.println(f1.filled_status());

		System.out.println(f2.book(90));
		System.out.println(f2.book(20));
		System.out.println(f2.filled_status());
	}
}
