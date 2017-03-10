#!/usr/bin/env zsh

git config --global credential.helper store
git config --global core.editor vim

mkdir ~/Git
cd ~/Git

echo '\nCloning Questionn'

git clone https://gitlab.com/GreenJoey/Questionarre.git/ ~/Git/questionn && cd questionn && git remote add bitbucket https://bitbucket.org/GreenJoey/questionn.git && git pull bitbucket master && cd ..

echo '\n\n\nCloning My-Simple-Programs\n'

git clone https://gitlab.com/GreenJoey/My-Simple-Programs.git && cd My-Simple-Programs && ln -s ~/Codes && cd ..

echo '\n\n\nCloning Blogg\n'

git clone https://bitbucket.org/GreenJoey/blogg.git/

echo '\n\n\nCloning Algo Implementations\n'

git clone https://github.com/GreenJoey/Algorithm-Implementations.git/

echo '\n\n\nCloning CPython\n'
git clone https://github.com/GreenJoey/cpython.git/
