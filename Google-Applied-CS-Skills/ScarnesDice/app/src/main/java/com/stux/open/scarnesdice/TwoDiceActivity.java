package com.stux.open.scarnesdice;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;

public class TwoDiceActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_two_dice);
    }

    public void roll_click (View view) {}

    public void hold_click (View view) {}

    public void reset_click (View view) {}
}
