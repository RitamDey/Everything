package com.google.codelabs.mdc.java.shrine.application;

import android.annotation.SuppressLint;
import android.app.Application;
import android.content.Context;
import android.support.v7.app.AppCompatDelegate;

public class ShrineApplication extends Application {
    @SuppressLint("StaticFieldLeak")
    private static ShrineApplication instance;
    private static Context appContext;

    public static ShrineApplication getInstance() {
        return instance;
    }

    public static Context getAppContext() {
        return appContext;
    }

    public void setAppContext(Context mAppContext) {
        this.appContext = mAppContext;
    }

    @Override
    public void onCreate() {
        super.onCreate();
        instance = this;

        this.setAppContext(getApplicationContext());
        AppCompatDelegate.setCompatVectorFromResourcesEnabled(true);
    }
}