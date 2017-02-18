<?php

    $var1 = 145;
    $var2 = 150;

    // Addition operator
    echo $var1 + $var2;
    echo "<br><br>";

    //Subtraction operator
    echo $var2 - $var1;
    echo "<br><br>";

    // Multiplication operator
    echo $var1 * $var2;
    echo "<br><br>";

    //Division operator
    echo $var2/$var1;
    echo "<br><br>";

    // Modulus operator
    echo $var1 % $var2;
    echo "<br><br>";

    // Increment and Decrement operators
    $var1--;
    $var2++;
    echo "$var1 $var2<br>";
    ++$var1;
    --$var2;
    echo "$var1 $var2";
    echo "<br><br>";

    // Power operations
    $x = 2;
    $y = 3;
    echo  $x**$y;
    echo "<br><br>";

    /*
    * Also PHP supports standard operator-assignment operations
    * like: +=, -=, *=, /= and %=
    */

    // Non-Equlaity Testing operators
    echo $var1 != $var2; // First operator way
    echo "<br>";
    echo $var1 <> $var2; // The other way
    echo "<br>";

    // Comparison operators
    echo $var1 < $var2;
    echo "<br>";
    echo $var2 > $var1;
    echo "<br>";

    $var1 = 5;
    $var2 = 5;
    //Equlaity test operators
    echo $var1 == $var2;
    echo "<br>";

    //Identity test operators
    echo $var1 === $var2;
    echo "<br>";
?>