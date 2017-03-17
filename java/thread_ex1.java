/**
 * This is an example of creating a thread using the Thread class
**/

class Loader extends Thread {
    public void run() {
        System.out.println("Hello ");
    }
}

class Thread1 {
    public static void main(String[] args) {
        Loader obj = new Loader();
        obj.start();
    }
}
