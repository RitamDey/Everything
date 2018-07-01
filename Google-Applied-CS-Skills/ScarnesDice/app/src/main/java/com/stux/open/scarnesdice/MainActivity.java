package com.stux.open.scarnesdice;

import android.graphics.drawable.Drawable;
import android.os.LocaleList;
import android.support.design.widget.FloatingActionButton;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
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

        ((TextView)findViewById(R.id.player_score)).setText("0");
        ((TextView)findViewById(R.id.computer_score)).setText("0");

        FloatingActionButton switcher = findViewById(R.id.modeSwitch);

        switcher.setOnClickListener( new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.i("com.stux.open.scarnesdice.FAB", "Floating button clicked");
            }
        });
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

    public void computerTurn() {
        // We can't enable or disable a button on runtime but we can make
        // it clickable or non-clickable using the `setClickable` API
        Button hold = findViewById(R.id.hold_button);
        hold.setClickable(false);

        Button reset = findViewById(R.id.reset_button);
        reset.setClickable(false);
        Integer score;

        while (this.computer_turn_score < 20) {
            score = this.random.nextInt(6);

            this.SetDice(score);
            Log.i("com.stux.open.scarnesdice.ComputerTurn", String.valueOf(score));

            if (score == 1) {
                this.computer_turn_score = 0;
                break;
            }

            this.computer_turn_score += score;

        }

        this.computer_score += computer_turn_score;

        TextView computer_score = findViewById(R.id.computer_score);
        computer_score.setText(String.format(LocaleList.getDefault().get(0), "%d", this.computer_score));

        hold.setClickable(true);
        reset.setClickable(true);
    }

    public void roll_click(View view) {
        Integer turn_score = this.random.nextInt(6) + 1;

        Log.println(Log.INFO,"com.stux.open.scarnesdice.roll_click", turn_score.toString());

        if (turn_score == 1) {
            this.user_turn_score = 0;
            this.computerTurn();
        }
        else
            this.user_turn_score += turn_score;

        this.SetDice(turn_score);
    }

    public void hold_click(View view) {
        this.user_score += this.user_turn_score;
        this.user_turn_score = 0;

        TextView user_score = findViewById(R.id.player_score);

        // Starting from Android 7.0 API 24, due to increased support for more Locale
        // Android exposes the LocaleList.getDefault() API which return a list of languages
        // the user has selected.
        user_score.setText(String.format(LocaleList.getDefault().get(0), "%d", this.user_score));

        this.computerTurn();
    }

    public void reset_click(View View) {
        this.computer_score = 0;
        this.computer_turn_score = 0;
        this.user_turn_score = 0;
        this.user_score = 0;

        TextView user_score = findViewById(R.id.player_score);
        user_score.setText("0");

        TextView computer_score = findViewById(R.id.computer_score);
        computer_score.setText("0");
    }
}
