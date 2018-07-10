package com.stux.open.scarnesdice;

import android.graphics.drawable.Drawable;
import android.os.LocaleList;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
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
        this.dice_2_view.setImageDrawable(getDrawable(R.drawable.d2));

        this.player_score_view.setText(String.format(LocaleList.getDefault().get(0), "%d", 0));
        this.computer_score_view.setText(String.format(LocaleList.getDefault().get(0), "%d", 0));
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

    private void computerTurn() {
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
}
