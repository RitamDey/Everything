package com.google.codelabs.mdc.java.shrine;

import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.design.button.MaterialButton;
import android.support.design.widget.TextInputEditText;
import android.support.design.widget.TextInputLayout;
import android.support.v4.app.Fragment;
import android.text.Editable;
import android.view.KeyEvent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

/**
 * Fragment representing the login screen for Shrine.
 */
public class LoginFragment extends Fragment {

    @Override
    public View onCreateView(
            @NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.shr_login_fragment, container, false);

        // Snippet from "Navigate to the next Fragment" section goes here.
        final TextInputLayout passwordTextInput = view.findViewById(R.id.password_text_input);
        final TextInputEditText passwordEditText = view.findViewById(R.id.password_edit_text);
        final TextInputEditText usernameEditText = view.findViewById(R.id.shr_username_edit);
        final TextInputLayout usernameLayout = view.findViewById(R.id.shr_username_input);
        MaterialButton nextButton = view.findViewById(R.id.next_button);

        // Set an error if the password is less than 8 characters
        nextButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                byte flag = 0;
                if (!isPasswordValid(passwordEditText.getText()))
                    flag += 2;
                if (!isUsernameValid(usernameEditText.getText()))
                    flag += 1;

                if (flag == 3) {
                    passwordTextInput.setError(getString(R.string.shr_error_password));
                    usernameLayout.setError(getString(R.string.shr_error_username));
                }
                else if (flag == 2)
                    passwordEditText.setError(getString(R.string.shr_error_password));
                else if (flag == 1)
                    usernameLayout.setError(getString(R.string.shr_error_username));
                else {
                    passwordTextInput.setError(null);
                    ((NavigationHost) getActivity()).navigateTo(new ProductGridFragment(), false);
                }
            }
        });

        // Clear the error once more than 8 characters are typed
        passwordEditText.setOnKeyListener(new View.OnKeyListener() {
            @Override
            public boolean onKey(View v, int keyCode, KeyEvent event) {
                if (!isPasswordValid(passwordEditText.getText())) {
                    passwordTextInput.setError(null);  // Clear the error
                }

                return false;
            }
        });

        // Clear error on username once entered
        usernameEditText.setOnKeyListener(new View.OnKeyListener() {
            @Override
            public boolean onKey(View v, int keyCode, KeyEvent event) {
                if (!isUsernameValid(usernameEditText.getText()))
                    usernameLayout.setError(null);
                return false;
            }
        });
        return view;
    }

    // "isPasswordValid" from "Navigate to the next Fragment" section method goes here
    private boolean isPasswordValid(@Nullable Editable text) {
        return text != null && text.length() >= 8;
    }
    private boolean isUsernameValid(@Nullable Editable username) {
        return username != null && username.length() > 0;
    }
}
