<?php
    // Variables are in global scope if they are declared in outside all functions

    $name = "Joe Green";

    // Variables declared in functions have a local scope
    function get_name() {
        global $name;
        $msg = "<b><i>Hello; $name !!!</i></b>";
        echo $msg;
    }

    get_name();
?>