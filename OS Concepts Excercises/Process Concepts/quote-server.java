import java.net.ServerSocket;
import java.net.Socket;
import java.io.PrintWriter;
import java.io.IOException;


class QuoteServer {
   public static void main(String[] args) {
       ServerSocket server = null;

       try {
       	   // Try to create a socket server that listens at port 6017
           server = new ServerSocket(6017);
       } catch (Exception err) {
           System.err.println(err);
       }

       // Try to accept for an incoming client connection and try to create a auto-flushing
       // stream out of the client connections's OutputStream
       try (Socket client = server.accept();
       	    PrintWriter writer = new PrintWriter(client.getOutputStream(), true);) {
           writer.println("Quote of the day here");
       } catch (IOException err) {
       	   System.err.println(err);
       }
   }
}
