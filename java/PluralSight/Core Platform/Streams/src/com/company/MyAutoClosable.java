package com.company;
import java.io.IOException;


public class MyAutoClosable implements AutoCloseable {
    public static void saySomething() throws IOException {
        System.out.println("This is a auto-closable class");
//        throw new IOException("These exceptions are suppressed.");
    }

    @Override
    public void close() throws IOException {
        throw new IOException("This is the closed method called");
    }
}
