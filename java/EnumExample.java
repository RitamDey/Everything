class FreshJuice {

    enum FreshJuiceSize{ SMALL, MEDIUM, LARGE}

    public static void main(String args[]){
	Object size;
        size = FreshJuiceEnum.FreshJuiceSize.MEDIUM;
        System.out.println("Size: "+size);
    }
}
