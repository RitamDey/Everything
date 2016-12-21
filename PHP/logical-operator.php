<?php

    $var1 = true;
    $var2 = false;

    // Logical and operators
    echo $var1 and $var2; // One way
    echo "<br>";
    echo $var1 && $var2; // Other way
    echo "<br>";

    // Logical or operator
    echo $var1 or $var2;
    echo "<br>";
    echo $var1 || $var2;
    echo "<br>";

    // Not operator
    echo !$var1;
    echo "<br>";
    echo !$var2;
    echo "<br>";

    // Xor operator
    // Returns `true` i.e if one of the operator is true but not both
    echo $var2 xor $var1;
    echo "<br>";
    echo !$var1 xor $var2;
    echo "<br>";
?>