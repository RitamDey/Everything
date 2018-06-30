package com.stux.open.scarnesdice;

import android.content.res.Resources;
import android.graphics.drawable.Drawable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.content.res.AppCompatResources;
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

        ((TextView)findViewById(R.id.player_score)).setText("0");
        ((TextView)findViewById(R.id.computer_score)).setText("0");
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


    public void roll_click(View view) {
        Integer turn_score = this.random.nextInt(6) + 1;

        Log.println(Log.INFO,"com.stux.open.scarnesdice.roll_click", turn_score.toString());

        if (turn_score == 1)
            this.user_turn_score = 0;
        else
            this.user_turn_score += turn_score;

        this.SetDice(turn_score);
    }
}
