//package Hangman;


//import Hangman.HangmanLexicon;
import java.util.Random;
import java.util.Arrays;

// Sun's private APIs for signal handling
import sun.misc.Signal;
import sun.misc.SignalHandler;

// Stanford ACM library
import acm.program.ConsoleProgram;
import acm.io.IOConsole;

public class Hangman extends ConsoleProgram {
  HangmanLexicon lexicon = new HangmanLexicon();
  char[] word;
  char[] guess;
  int retries;
  Random generator = new Random();


  void setWord() {
    // Get the total words in the lexicon
    int total = this.lexicon.getWordCount();

    // Generate a random number between 0 and total (exclusive)
    int index = this.generator.nextInt(total);

    // Set the randomly selected word and prepare the guess holder
    this.word = this.lexicon.getWord(index).toCharArray();
    this.guess = new char[this.word.length];

    Arrays.fill(this.guess, '_');

    this.retries = 8;
    this.println(this.word);
  }

  String display() {
    this.print("The word now looks like this: ");
    this.println(Arrays.toString(this.guess));
    if (this.retries == 1)
      this.println("You have only one guess left.");
    else
      this.println("You have " + this.retries + " guesses left");
    return "Your guess: ";
  }

  int find(char ch) {
    boolean found = false;
    int pos = -2;

    for (int i=0; i < this.word.length; ++i) {
      if (this.word[i] == ch) {
        found = true;
        if (this.guess[i] == '_')
          pos = i;
      }
    }

    return ( found == true) ? pos:-1;
  }

  public void run() {
    this.setWord();
    while (this.retries > 0) {
      // Get the input, validate it and convert to char
      String str = this.readLine(this.display()).toUpperCase();

      while (str.length() == 0 || str.length() > 1) {
        this.println("Invalid guess");
        str = this.console.readLine("Guess again: ").toUpperCase();
      }

      char ch = str.charAt(0);

      // Find the index of the char if a correct guess is made
      // Or reduce the retries by one
      int index = this.find(ch);

      if (index == -1) {
        this.retries -= 1;
        System.out.printf("There are no %c's in word\n", ch);
      }
      else if (index == -2)
        this.println("That guess is correct.");
      else {
        this.guess[index] = ch;
        this.println("That guess is correct");
      }

      // After the guess array is updated, check to see
      // if both of them are equal. If so the player has guessed
      // the word correctly, end the game
      if (Arrays.equals(this.word, this.guess)) {
        this.print("You guessed the word: ");
        this.println(Arrays.toString(this.word));
        this.println("You win.");
        return;
      }
    }

    // If we reach here then the player hasn't guessed the word
    // Indicate he lost the game
    this.println("You're completely hung.");
    this.print("The word was: ");
    this.println(Arrays.toString(this.word));
    this.println("You lose.");
  }
}


class Game {
  public static void main(String[] args) {
    Hangman game = new Hangman();
    game.init();

    Signal.handle(new Signal("INT"), new SignalHandler() {
      public void handle(Signal sig) {
        System.out.println("\nExiting Game");
        System.exit(0);
      }
    });

    while (true) {
      game.run();
    }
  }
}
