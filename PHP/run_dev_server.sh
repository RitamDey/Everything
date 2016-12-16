#!/usr/bin/env bash

read script_name

echo "Running PHP development server for $script_name script\n"

php -S 127.0.0.2:8000 $script_name
