/* Copyright 2016 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.engedu.anagrams;

import android.support.annotation.NonNull;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;
import java.util.HashSet;
import java.util.HashMap;
import java.util.Random;

public class AnagramDictionary {

    private static final int MIN_NUM_ANAGRAMS = 5;
    private static final int DEFAULT_WORD_LENGTH = 3;
    private static final int MAX_WORD_LENGTH = 7;
    private static int wordLength = DEFAULT_WORD_LENGTH;

    private Random random = new Random();
    private ArrayList<String> wordList = new ArrayList<>();
    private HashSet<String> wordSet = new HashSet<>();
    private HashMap<String, ArrayList<String>> lettersToWord = new HashMap<>();
    private HashMap<Integer, ArrayList<String>> sizeToWords = new HashMap<>();

    public AnagramDictionary(Reader reader) throws IOException {
        BufferedReader in = new BufferedReader(reader);
        String line;
        String sorted;

        while((line = in.readLine()) != null) {
            String word = line.trim();
            sorted = this.sortLetters(word);
            int len = word.length();
            this.wordList.add(word);

            if (!this.lettersToWord.containsKey(sorted))
                this.lettersToWord.put(sorted, new ArrayList<String>());

            if (!this.sizeToWords.containsKey(len))
                this.sizeToWords.put(len, new ArrayList<String>());

            this.lettersToWord.get(sorted).add(word);
            this.sizeToWords.get(len).add(word);

            this.wordSet.add(word);
        }
    }

    public boolean isGoodWord(String word, String base) {
        return this.wordSet.contains(word) && !word.contains(base);
    }

    @NonNull
    private String sortLetters(String input) {
        char[] res = input.toCharArray();

        for (int pos = 0; pos < res.length; ++pos) {
            char key = res[pos];
            int j = pos;

            while (j > 0 && res[j-1] > key) {
                res[j] = res[j-1];
                j--;
            }

            res[j] = key;
        }

        return String.valueOf(res);
    }

    public List<String> getAnagrams(String targetWord) {
        ArrayList<String> result = new ArrayList<>();
        targetWord = this.sortLetters(targetWord);

        for (String word : this.wordList) {
            if (word.length() == targetWord.length() &&
                    targetWord.equals(sortLetters(word)))
                result.add(word);
        }

        return result;
    }

    public List<String> getAnagramsWithOneMoreLetter(String word) {
        ArrayList<String> result = new ArrayList<>();
        String target = word;

        for (char ch : "abcdefghijklmnopqrstuvwxyz".toCharArray()) {
            target = this.sortLetters(word + ch);

            if (this.lettersToWord.containsKey(target)) {
                for (String str:
                        this.lettersToWord.get(target)) {
                    if (this.isGoodWord(str, word))
                        result.add(str);
                }
            }
        }
        return result;
    }


    public String pickGoodStarterWord() {
        ArrayList<String> words = this.sizeToWords.get(wordLength);
        int random = this.random.nextInt(words.size());
        String res = "";

        for (int i = random; i < words.size(); i = (i+1)%words.size()) {
            List<String> words_list = this.getAnagramsWithOneMoreLetter(
                    words.get(i)
            );

            if (words_list.size() >= MIN_NUM_ANAGRAMS) {
                res = words.get(i);
                break;
            }
        }

        if (wordLength <= MAX_WORD_LENGTH)
            wordLength++;

        return res;
    }
}
