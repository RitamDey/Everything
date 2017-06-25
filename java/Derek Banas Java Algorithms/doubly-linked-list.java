class Neighbour {
    public String homeOwnerName;
    public int houseNumber;

    public Neighbour next;
    public Neighbour previous;

    public Neighbour(String homeOwnerName, int houseNumber) {
        this.homeOwnerName = homeOwnerName;
        this.houseNumber = houseNumber;
    }

    public void display() {
        System.out.println(this.houseOwnerName + " : "+ this.houseNumber);
    }

    public String toString() {
        return this.houseOwnerName;
    }
}
