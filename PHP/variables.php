<?php
    // Normal variable declaration
    $name = "John";
    // Constant declaration
    define("age", 25, true);
    // Printing variables to the HTML document
    echo "$name is of age ";
    // Constants can't be printed in the above way. They are done using this syntax
    echo age;
    echo "<br><br>";

    // $$<var name> is used to declare a variable that points to another variable
     $name_ptr = 'name';

     echo $$name_ptr;
?>