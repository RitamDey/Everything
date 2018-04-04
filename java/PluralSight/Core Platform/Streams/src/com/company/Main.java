package com.company;

import java.io.IOException;
import java.io.Reader;
import java.io.Writer;

import com.company.Helper;


public class Main {
    public static void TryCatchFinally() {
        char[] buff = new char[8];
        int length;
        Reader reader = null;

        try {
            reader = Helper.openReader("text.txt");
            while ((length = reader.read(buff)) >= 0) {
                System.out.println("\nLength: " + length);
                for(int i = 0; i < length; ++i) {
                    System.out.println(buff[i]);
                }
            }
        } catch (IOException e) {
            System.out.println(e.getClass().getSimpleName() + " - " + e.getMessage());
        } finally {
            try {
                if (reader != null)
                    reader.close();
            } catch (IOException e2) {
                System.out.println(e2.getClass().getSimpleName() + " - " + e2.getMessage());
            }
        }
    }

    public static void TryWithResource() {
        char[] buff = new char[8];
        int length;

        // By this way we are letting try-block know about the Resource we are using so that it free it
        try (Reader reader = Helper.openReader("text.txt")) {
            while ((length = reader.read(buff)) >= 0) {
                System.out.println("\nLength: " + length);
                for(int i = 0; i < length; ++i)
                    System.out.println(buff[i]);
            }
        } catch (IOException e) {
            System.out.println(e.getClass().getSimpleName() + " - " + e.getMessage());
        }
    }

    public static void TryWithResourceMulti() {
        char[] buff = new char[8];
        int length;

        // By this way we are letting try-block know about the multiple Resources we are using so that it free it
        try (Reader reader = Helper.openReader("text.txt");
             Writer writer = Helper.openWriter("out.txt")) {
            while ((length = reader.read(buff)) >= 0) {
                System.out.println("\nLength: " + length);
                writer.write(buff, 0, length); // write out the buffer from 0 index to max read in
            }
        } catch (IOException e) {
            System.out.println(e.getClass().getSimpleName() + " - " + e.getMessage());
        }
    }

    public static void doCloseThing() {
        try (MyAutoClosable obj = new MyAutoClosable()) {
            obj.saySomething();
        } catch (IOException e) {
            System.out.println(e.getClass().getSimpleName() + " - " + e.getMessage());

            for (Throwable err: e.getSuppressed())  // Get the errors suppressed
                System.out.println(err.getClass().getSimpleName() + " - " + err.getMessage());
        }
    }

    public static void main(String[] args) {
        TryCatchFinally();
        TryWithResource();
        TryWithResourceMulti();
        doCloseThing();
    }
}
