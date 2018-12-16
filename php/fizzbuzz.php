<html>
<body>
    <center>
        <h1>
<?php
function fizzbuzz($num) {
    if ($num%3 == 0)
        echo "Fizz";

    if ($num%5 == 0)
        echo "Buzz";

    echo "!<br>";
}

for ($var=1; $var <= 100; ++$var)
    echo $var, " ", fizzbuzz($var);
?>
        </h1>
    </center>
</body>
</html>
