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

package com.google.engedu.wordstack;

import android.app.Activity;
import android.content.res.AssetManager;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.DragEvent;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Random;
import java.util.Stack;

public class MainActivity extends Activity {

    private static final int WORD_LENGTH = 5;
    public static final int LIGHT_BLUE = Color.rgb(176, 200, 255);
    public static final int LIGHT_GREEN = Color.rgb(200, 255, 200);
    private ArrayList<String> words = new ArrayList<>();
    private Random random = new Random();
    private StackedLayout stackedLayout;
    private String word1, word2;
    private Stack<LetterTile> letterTileStack = new Stack<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        AssetManager assetManager = getAssets();
        try {
            InputStream inputStream = assetManager.open("words.txt");
            BufferedReader in = new BufferedReader(new InputStreamReader(inputStream));
            String line = null;
            while((line = in.readLine()) != null) {
                String word = line.trim();

                if (word.length() == MainActivity.WORD_LENGTH)
                    words.add(word);
            }
        } catch (IOException e) {
            Toast toast = Toast.makeText(this, "Could not load dictionary", Toast.LENGTH_LONG);
            toast.show();
        }
        LinearLayout verticalLayout = (LinearLayout) findViewById(R.id.vertical_layout);
        stackedLayout = new StackedLayout(this);
        verticalLayout.addView(stackedLayout, 3);
        stackedLayout.setOnDragListener(new View.OnDragListener() {
            @Override
            public boolean onDrag(View view, DragEvent event) {
                int action  = event.getAction();
                if (action == DragEvent.ACTION_DRAG_STARTED)
                    return true;
                else if (action == DragEvent.ACTION_DROP) {
                    LetterTile tile = (LetterTile) event.getLocalState();
                    tile.moveToViewGroup(stackedLayout);

                    letterTileStack.remove(tile);

                    if (!letterTileStack.empty())
                        letterTileStack.peek().unfreeze();

                    Log.i(MainActivity.class.getCanonicalName(), letterTileStack.toString());
                    return true;
                }

                return false;
            }
        });

        View word1LinearLayout = findViewById(R.id.word1);
        word1LinearLayout.setOnDragListener(new DragListener());
        View word2LinearLayout = findViewById(R.id.word2);
        word2LinearLayout.setOnDragListener(new DragListener());
    }


    private class DragListener implements View.OnDragListener {

        public boolean onDrag(View v, DragEvent event) {
            int action = event.getAction();

            switch (action) {
                case DragEvent.ACTION_DRAG_STARTED:
                    v.setBackgroundColor(LIGHT_BLUE);
                    v.invalidate();
                    return true;
                case DragEvent.ACTION_DRAG_ENTERED:
                    v.setBackgroundColor(LIGHT_GREEN);
                    v.invalidate();
                    return true;
                case DragEvent.ACTION_DRAG_EXITED:
                    v.setBackgroundColor(LIGHT_BLUE);
                    v.invalidate();
                    return true;
                case DragEvent.ACTION_DRAG_ENDED:
                    v.setBackgroundColor(Color.WHITE);
                    v.invalidate();
                    return true;
                case DragEvent.ACTION_DROP:
                    // Dropped, reassign Tile to the target Layout

                    LetterTile tile = (LetterTile)((LinearLayout)v).getChildAt(
                            ((LinearLayout)v).getChildCount() - 1
                    );

                    if (tile != null)
                        tile.freeze();

                    tile = (LetterTile) event.getLocalState();
                    tile.moveToViewGroup((ViewGroup) v);

                    if (stackedLayout.empty()) {
                        TextView messageBox = (TextView) findViewById(R.id.message_box);
                        messageBox.setText(String.format("%s %s", word1, word2));
                    }


                    letterTileStack.push(tile);

                    Log.i(MainActivity.class.getCanonicalName(), letterTileStack.toString());
                    tile.unfreeze();
                    return true;
            }
            return false;
        }
    }

    public boolean onStartGame(View view) {
        this.stackedLayout.clear();
        ((LinearLayout)findViewById(R.id.word1)).removeAllViews();
        ((LinearLayout)findViewById(R.id.word2)).removeAllViews();

        TextView messageBox = (TextView) findViewById(R.id.message_box);
        messageBox.setText(R.string.game_started);
        StringBuilder random = new StringBuilder();

        int word1_count = 0;
        int word2_count = 0;

        this.word1 = this.words.get(this.random.nextInt(this.words.size()));
        Log.i(MainActivity.class.getSimpleName(), "First word is " + this.word1);


        this.word2 = this.words.get(this.random.nextInt(this.words.size()));
        Log.i(MainActivity.class.getSimpleName(), "Second word is " + this.word2);

        char chosen;

        while (word1_count < this.word1.length() && word2_count < this.word2.length()) {
            if (this.random.nextBoolean()) {
                chosen = this.word1.charAt(word1_count);
                word1_count++;
            }
            else {
                chosen = this.word2.charAt(word2_count);
                word2_count++;
            }

            random.append(chosen);
        }

        while (word1_count < this.word1.length()) {
            chosen = this.word1.charAt(word1_count);

            random.append(chosen);

            word1_count++;
        }
        while (word2_count < this.word2.length()) {
            chosen = this.word2.charAt(word2_count);
            random.append(chosen);

            word2_count++;
        }

        messageBox.setText(random.toString());

        for (int pos=random.length() - 1; pos >= 0; --pos)
            this.stackedLayout.push(new LetterTile(this, random.charAt(pos)));

        Log.i(MainActivity.class.getSimpleName(), this.stackedLayout.toString());
        return true;
    }

    public boolean onUndo(View view) {
        if (!this.letterTileStack.empty()) {
            LetterTile tile = this.letterTileStack.pop();

            tile.moveToViewGroup(this.stackedLayout);
        }
        return true;
    }
}
