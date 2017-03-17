package com.stux.helloworld;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.text.Editable;
import android.view.Gravity;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void magic(View view){
        TextView msg = (TextView)findViewById(R.id.message); //Get reference to the TextView
        EditText in = (EditText)findViewById(R.id.editText); //Get reference to the TextFeild
        CharSequence new_msg = "Hello "+in.getText()+"!!!";
        /*Create the message as a CharSequence as Strings are incompatible in .setText() and .makeText()*/
        msg.setText(new_msg); //Set the text to the new message
        Toast toast = Toast.makeText(this, new_msg, Toast.LENGTH_LONG); // Create a new Toast object
        toast.setGravity(Gravity.CENTER, 0, 0); //Set its postition on screen
        toast.show(); //Show It
    }
}
