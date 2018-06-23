//package Hangman;


//import Hangman.HangmanLexicon;
import java.util.Random;
import java.util.Arrays;
import java.util.Scanner;


public class Hangman {
  HangmanLexicon lexicon = new HangmanLexicon();
  char[] word;
  char[] guess;
  int retries;
  Random generator = new Random();
  Scanner sc = new Scanner(System.in);


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
    System.out.println(this.word);
  }

  void display() {
    System.out.print("The word now looks like this: ");
    System.out.println(Arrays.toString(this.guess));
    if (this.retries == 1)
      System.out.println("You have only one guess left.");
    else
      System.out.printf("You have %d guesses left\n", this.retries);
    System.out.print("Your guess: ");
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
      this.display();

      // Get the input, validate it and convert to char
      String str = this.sc.nextLine().toUpperCase();

      while (str.length() == 0 || str.length() > 1) {
        System.out.println("Invalid guess");
        System.out.print("Guess again: ");
        str = this.sc.nextLine().toUpperCase();
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
        System.out.println("That guess is correct.");
      else {
        this.guess[index] = ch;
        System.out.println("That guess is correct");
      }

      // After the guess array is updated, check to see
      // if both of them are equal. If so the player has guessed
      // the word correctly, end the game
      if (Arrays.equals(this.word, this.guess)) {
        System.out.print("You guessed the word: ");
        System.out.println(Arrays.toString(this.word));
        System.out.println("You win.");
        return;
      }
    }

    // If we reach here then the player hasn't guessed the word
    // Indicate he lost the game
    System.out.println("You're completely hung.");
    System.out.print("The word was: ");
    System.out.println(Arrays.toString(this.word));
    System.out.println("You lose.");
  }
}


class Game {
  public static void main(String[] args) {
    Hangman game = new Hangman();

    while (true) {
      game.run();
    }
  }
}
