package com.company;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.Reader;
import java.io.Writer;

public class Helper {
    public static Reader openReader(String name) throws IOException{
        return Files.newBufferedReader(Paths.get(name));
    }

    public static Writer openWriter(String name) throws IOException{
        return Files.newBufferedWriter(Paths.get(name));
    }
}
