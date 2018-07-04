package com.stux.open.scarnesdice;

import android.graphics.drawable.Drawable;
import android.os.LocaleList;
import android.support.design.widget.FloatingActionButton;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;


import java.util.Random;


public class MainActivity extends AppCompatActivity {
    private Integer user_score = 0;
    private Integer computer_score = 0;
    private Integer user_turn_score = 0;
    private Integer computer_turn_score = 0;


    private final Random random = new Random();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        FloatingActionButton switcher = findViewById(R.id.modeSwitch);

        switcher.setOnClickListener( new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // TODO: Use the FAB to take user to 2-dice mode
                Log.i("com.stux.open.scarnesdice.FAB", "Floating button clicked");
            }
        });

        TextView player = findViewById(R.id.player_score);
        TextView computer = findViewById(R.id.computer_score);

        /*
         * `TextWatcher` objects are attached to objects of type `Editable`.
         * They are called when the text in the `Editable` object changes. Use them here to watch the
         * score views and terminate the game when either the player or computer scores >= 100
         */
        TextWatcher score_watcher = new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
                // Called to notify that somewhere within s, text is being changed
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                /*
                 * Called just after old text within `s` has been replaced
                 * starting from `start` and had length `before`
                */
            }

            @Override
            public void afterTextChanged(Editable s) {
                // Called to notify that somewhere within s, text has changed
                if (Integer.parseInt(s.toString()) >= 100) {
                    /*
                     * Convert the `Editable` to `Integer` and check whether it's
                     * greater than or equal to 100. If so the game has ended.
                     * Disable the `Roll` and `Hold` button
                    */
                    findViewById(R.id.hold_button).setClickable(false);
                    findViewById(R.id.roll_button).setClickable(false);
                }
            }
        };

        /*
         * Set the score board to 0 and then add text change listeners
         * Do it before adding listeners to avoid useless calls to listeners
         * even before any actual update to game score has been done.
        */
        player.setText(String.format(LocaleList.getDefault().get(0), "%d", 0));
        computer.setText(String.format(LocaleList.getDefault().get(0), "%d", 0));

        player.addTextChangedListener(score_watcher);
        computer.addTextChangedListener(score_watcher);

    }

    private void SetDice(Integer value) {
        ImageView dice_view = findViewById(R.id.dice_view);

        Log.println(Log.INFO, "com.stux.open.scarnesdice.SetDice", String.valueOf(value));
        Drawable dice;

        if (value == 1)
            dice = getResources().getDrawable(R.drawable.d1, getApplicationContext().getTheme());
        else if(value == 2)
            dice = getResources().getDrawable(R.drawable.d2, getApplicationContext().getTheme());
        else if (value == 3)
            dice = getResources().getDrawable(R.drawable.d3, getApplicationContext().getTheme());
        else if (value == 4)
            dice = getResources().getDrawable(R.drawable.d4, getApplicationContext().getTheme());
        else if (value == 5)
            dice = getResources().getDrawable(R.drawable.d5, getApplicationContext().getTheme());
        else
            dice = getResources().getDrawable(R.drawable.d6, getApplicationContext().getTheme());

        dice_view.setImageDrawable(dice);
    }

    private void computerUpdate() {
        this.computer_score += this.computer_turn_score;
        this.computer_turn_score = 0;

        /*
          * Here we first get the `TextView`, then we set the Hold to clickable.
          * This is important because if the Hold button is turned after update to the `TextView`
          * then it turns the Hold button clickable again thus partially defeating the purpose of the
          * Text Watchers of the `TextView`
         */
        TextView computer_score = findViewById(R.id.computer_score);

        findViewById(R.id.hold_button).setClickable(true);

        computer_score.setText(String.format(LocaleList.getDefault().get(0), "%d", this.computer_score));

        findViewById(R.id.reset_button).setClickable(true);
    }


    private void computerTurn() {
        // TODO: Complete the documentation along with `Handler` documentation
        findViewById(R.id.hold_button).setClickable(false);
        findViewById(R.id.reset_button).setClickable(false);



    }

    public void roll_click(View view) {
        /*
         * This method handles the Roll button click event for single dice mode
         * It starts by getting a random number representing the the user's dice roll score. The it
         * checks if the rolled dice score is equals to 1 or not. If it's one, the terminate the user
         * turn, 0 the player's turn score and let the computer have its turn. If not then add the
         * roll score to the user's turn score.
         * Finally to set the dice face view to the appropriate dice face image
         */

        Integer turn_score = this.random.nextInt(6) + 1;

        Log.println(Log.INFO,"com.stux.open.scarnesdice.roll_click", turn_score.toString());

        this.SetDice(turn_score);

        if (turn_score == 1) {
            this.user_turn_score = 0;
            try {
                // Sleep just for the user to notice he/she rolled a 1
                Thread.sleep(1700);
            } catch (InterruptedException ignored) {}

            this.computerTurn();
        }
        else
            this.user_turn_score += turn_score;

    }

    public void hold_click(View view) {
        /*
         * Handles the Hold button click event for the single dice mode.
         * It starts by adding the player's current turn score to his total game score
         * Then goes on to update the required `TextView` by converting the `Integer` score to
         * `String` using `.format()` method with the locale set to the system's first default locale
         * And then it invokes the computer's turn
         */

        this.user_score += this.user_turn_score;
        this.user_turn_score = 0;

        TextView user_score = findViewById(R.id.player_score);

        /*
         * Starting from Android 7.0 API 24, due to increased support for more Locale
         * Android exposes the LocaleList.getDefault() API which return a list of languages
         * the user has selected.
        */
        user_score.setText(String.format(LocaleList.getDefault().get(0), "%d", this.user_score));

        this.computerTurn();
    }

    public void reset_click(View View) {
        /*
         * Handles the Reset button click event for the single dice mode
         * It starts by 0-ing the scores of player and computer and then moves to updating the
         * score `TextView`s
         * After that it moves to set Roll button and Hold button clickable again.
         * Then it moves to update the dice face `ImageView` to display the dice face 1
         */

        this.computer_score = 0;
        this.computer_turn_score = 0;
        this.user_turn_score = 0;
        this.user_score = 0;

        TextView user_score = findViewById(R.id.player_score);
        user_score.setText(String.format(LocaleList.getDefault().get(0), "%d", 0));

        TextView computer_score = findViewById(R.id.computer_score);
        computer_score.setText(String.format(LocaleList.getDefault().get(0), "%d", 0));

        findViewById(R.id.roll_button).setClickable(true);
        findViewById(R.id.hold_button).setClickable(true);

        ((ImageView)findViewById(R.id.dice_view)).setImageDrawable(getDrawable(R.drawable.d1));
    }
}
