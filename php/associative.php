<html>
<body>
    <center>
        <h1>
<?php
$friends = array (
    "sTux" => "IT",
    "Polu" => "Clicking",
    "Soumik" => "Coding",
    "Everybody else" => "Life",
);

foreach ($friends as $person => $fav_thing) {
    echo $person, " likes ", $fav_thing, "<br>";
}
?>
        </h1>
    </center>
</body>
</html>
