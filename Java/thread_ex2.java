/**
 * This is a example of creating thread by implementing the Runnable interface
**/

class Loader implements Runnable {
    public void run() {
        System.out.println("Hello");
    }
}

class Thread2 {
    public static void main(String[] args) {
        // In this case the thread object needs to be a Thread object and object of the threaded class needs to be passed as parameter
        Thread obj = new Thread(new Loader());
        obj.start();
    }
}
