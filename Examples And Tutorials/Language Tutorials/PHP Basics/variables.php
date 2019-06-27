<html>
<body>

    <center>
        <h1>
<?php
        // All variables start with "$"
        $first_name = "sTux";  // This is a string type
        $age = 20;  // This is a decimal type
        $price = 19.25; // This is a float type
        $alive = TRUE;  // This is a boolean type

        echo "$first_name is $age years old";

        echo "PHP types are 
            <ul>
                <li> ", gettype($first_name)," </li>
                <li> ", gettype($age), " </li>
                <li> ", gettype($price), " </li>
                <li> ", gettype($alive), " </li>
            </ul>";
?>
        </h1>
    </center>
</body>
</html>
