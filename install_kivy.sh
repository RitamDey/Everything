#!/usr/bin/env bash

echo "Enter the root password when asked"

su -c "pip install cython && pip install hg+http://bitbucket.org/pygame/pygame && pip install kivy"

echo "Kivy is installed"
