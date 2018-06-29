package com.example.stux.helloworldapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    public static final String EXTRA_MESSAGE = "com.example.stux.helloworldapp.MESSAGE";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    // Called when the Send button is pressed
    public void sendMessage(View view) {
        // An Intent is an object that provides runtime binding between separate components,
        // such as two activities. The Intent represents an app’s "intent to do something."
        // You can use intents for a wide variety of tasks, but in this lesson,
        // your intent starts another activity.

        // `Intent` constructor takes 2 parameters:
        // A Context, here this is used as `Activity` class is a subclass of `Context`
        // A class of the app component to which the system should deliver the intent
        Intent intent = new Intent(this, DisplayMessageActivity.class);
        EditText editText = (EditText) findViewById(R.id.editText);
        String message = editText.getText().toString();

        // The `putExtra()` method add key-value pairs to an Intent, called extras.
        // The key is a public constant, which the next activity uses to retrieve value
        // It is a good practice to define keys using app's package name,
        // as it ensures the keys to be unique.
        intent.putExtra(EXTRA_MESSAGE, message);

        startActivity(intent);
    }
}
