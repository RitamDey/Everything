import java.util.*;
import java.io.*;

public class ideone
{
public static void main(String[] args)
{
Scanner in = new Scanner(System.in);
//int max=in.nextInt();
for(int n=0,max=in.nextInt();n<=max;n++)
{
 String give=in.nextWord();
 int k=give.length()/2;
 System.out.println(give.length());
   for(int b=0;b<=k;b++)
   {
    if(b%2==0)
    {
     System.out.print(give.charAt(b));
    }
   }
  }
 }
}
