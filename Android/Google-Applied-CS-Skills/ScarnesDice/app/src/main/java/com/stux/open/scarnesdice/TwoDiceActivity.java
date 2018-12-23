package com.stux.open.scarnesdice;

import android.graphics.drawable.Drawable;
import android.os.Handler;
import android.os.LocaleList;
import android.os.PersistableBundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.Random;

public class TwoDiceActivity extends AppCompatActivity {
    private final Random dice_1 = new Random();
    private final Random dice_2 = new Random();
    private final String TAG = TwoDiceActivity.class.getSimpleName();

    private Integer player_score = 0;
    private Integer player_turn_score = 0;
    private Integer computer_score = 0;
    private Integer computer_turn_score = 0;

    private ImageView dice_1_view = null;
    private ImageView dice_2_view = null;
    private TextView player_score_view = null;
    private TextView computer_score_view = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_two_dice);

        this.dice_1_view = findViewById(R.id.dice1_view);
        this.dice_2_view = findViewById(R.id.dice2_view);

        this.player_score_view = findViewById(R.id.player_score);
        this.computer_score_view = findViewById(R.id.computer_score);

        this.dice_1_view.setImageDrawable(getDrawable(R.drawable.d1));
        this.dice_2_view.setImageDrawable(getDrawable(R.drawable.d1));

        this.player_score_view.setText(String.format(LocaleList.getDefault().get(0), "%d", 0));
        this.computer_score_view.setText(String.format(LocaleList.getDefault().get(0), "%d", 0));

//        (findViewById(R.id.textView)).setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                ((TextView)v).setText("");
//            }
//        });

        TextWatcher game_finish = new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
                if (Integer.parseInt(s.toString()) >= 100) {
                    findViewById(R.id.roll_button).setClickable(false);
                    findViewById(R.id.hold_button).setClickable(false);
                }
            }
        };

        this.player_score_view.addTextChangedListener(game_finish);
        this.computer_score_view.addTextChangedListener(game_finish);

        if (savedInstanceState != null) {
            Log.i(this.TAG, "Restoring");

            this.player_score = savedInstanceState.getInt("player_score");
            this.computer_score = savedInstanceState.getInt("computer_score");
        }
    }

    private void setDice (@NonNull Integer v1, Integer v2) {
        Drawable dice = null;

        switch (v1) {
            case 1:
                dice = getDrawable(R.drawable.d1);
                break;
            case 2:
                dice = getDrawable(R.drawable.d2);
                break;
            case 3:
                dice = getDrawable(R.drawable.d3);
                break;
            case 4:
                dice = getDrawable(R.drawable.d4);
                break;
            case 5:
                dice = getDrawable(R.drawable.d5);
                break;
            case 6:
                dice = getDrawable(R.drawable.d6);
                break;
        }

        this.dice_1_view.setImageDrawable(dice);

        switch (v2) {
            case 1:
                dice = getDrawable(R.drawable.d1);
                break;
            case 2:
                dice = getDrawable(R.drawable.d2);
                break;
            case 3:
                dice = getDrawable(R.drawable.d3);
                break;
            case 4:
                dice = getDrawable(R.drawable.d4);
                break;
            case 5:
                dice = getDrawable(R.drawable.d5);
                break;
            case 6:
                dice = getDrawable(R.drawable.d6);
                break;
        }

        this.dice_2_view.setImageDrawable(dice);
    }

    private void computerUpdate() {
        findViewById(R.id.roll_button).setClickable(true);
        findViewById(R.id.hold_button).setClickable(true);
        findViewById(R.id.reset_button).setClickable(true);

        this.computer_score += this.computer_turn_score;
        this.computer_turn_score = 0;

        this.computer_score_view.setText(String.format(LocaleList.getDefault().get(0), "%d", this.computer_score));
    }

    private void computerTurn() {
        findViewById(R.id.roll_button).setClickable(false);
        findViewById(R.id.hold_button).setClickable(false);
        findViewById(R.id.reset_button).setClickable(false);

        final Handler handler = new Handler();

        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                Integer roll1 = dice_1.nextInt(6) + 1;
                Integer roll2 = dice_2.nextInt(6) + 1;

                setDice(roll1, roll2);

                Log.i(TAG, "Computer scored " + roll1 + " " + roll2);

                if (roll1.equals(1) && roll2.equals(1)) {
                    computer_turn_score = 0;
                    computer_score = 0;

                    computer_score_view.setText(String.format(LocaleList.getDefault().get(0), "%d", 0));

                    computerUpdate();
                }

                else if (roll1.equals(1) || roll2.equals(1)) {
                    computer_turn_score = 0;

                    computerUpdate();
                }

                else {
                    computer_turn_score += roll1 + roll2;

                    if ((roll1.equals(6) && roll2.equals(6)) || computer_turn_score < 20)
                        handler.postDelayed(this, 500);
                    else
                        computerUpdate();
                }
            }
        }, 0);
    }

    public void roll_click (View view) {
        Integer roll_1 = this.dice_1.nextInt(6) + 1;
        Integer roll_2 = this.dice_2.nextInt(6) + 1;

        Log.i(this.TAG, "Player rolled " + roll_1.toString() + " " + roll_2.toString());

        this.setDice(roll_1, roll_2);

        if (roll_1.equals(1) && roll_2.equals(1)) {
            this.player_turn_score = 0;
            this.player_score = 0;

            this.player_score_view.setText(String.format(LocaleList.getDefault().get(0), "%d", 0));

            this.computerTurn();
        }

        else if (roll_1.equals(1) || roll_2.equals(1)) {
            this.player_turn_score = 0;

            this.computerTurn();
        }

        else {
            this.player_turn_score += roll_1 + roll_2;

            if (roll_1.equals(6) && roll_2.equals(6))
                findViewById(R.id.roll_button).performClick();
        }
    }

    public void hold_click (View view) {
        this.player_score += this.player_turn_score;
        this.player_turn_score = 0;

        Log.i(this.TAG, "User score is " + this.player_score);

        this.player_score_view.setText(String.format(LocaleList.getDefault().get(0), "%d", this.player_score));

        if (this.player_score < 100)
            this.computerTurn();
    }

    public void reset_click (View view) {
        this.player_score = 0;
        this.player_turn_score = 0;
        this.computer_score = 0;
        this.computer_turn_score = 0;

        this.player_score_view.setText(String.format(LocaleList.getDefault().get(0), "%d", this.player_score));
        this.computer_score_view.setText(String.format(LocaleList.getDefault().get(0), "%d", this.computer_score));

        this.dice_1_view.setImageDrawable(getDrawable(R.drawable.d1));
        this.dice_2_view.setImageDrawable(getDrawable(R.drawable.d1));
    }

    @Override
    public void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);

        outState.putInt("player_score", this.player_score);
        outState.putInt("computer_score", this.computer_score);
    }

    @Override
    protected void onRestoreInstanceState(Bundle savedInstanceState) {
        super.onRestoreInstanceState(savedInstanceState);

        Log.i(this.TAG, "Restoring");

        this.player_score = savedInstanceState.getInt("player_score");
        this.computer_score = savedInstanceState.getInt("computer_score");
    }
}
