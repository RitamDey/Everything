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
        TextView msg = (TextView)findViewById(R.id.message);
        EditText in = (EditText)findViewById(R.id.editText);
        CharSequence new_msg = "Hello "+in.getText()+"!!!";
        msg.setText(new_msg);
        Toast toast = Toast.makeText(this, new_msg, Toast.LENGTH_LONG);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }
}
