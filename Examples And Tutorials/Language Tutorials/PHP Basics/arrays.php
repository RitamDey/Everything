<html>
<body>
    <center>
        <h1>
<?php
        $name = "sTux";
        $friends = array("John", "Tim", "Tina", $name);

        echo count($friends), "<br>"; // Gets the length

        echo $friends[count($friends) - 1];

        echo "<ul>";

        foreach ($friends as $friend) {
            echo "<li>", $friend, "</li>";
        }

        $num = 0;
        while ($num < count($friends)) {
            echo "<b><i>", $friends[$num], "</b></i><br>";
            $num++;
        }

        echo "</ul>";
?>
        </h1>
    </center>
</body>
</html>
