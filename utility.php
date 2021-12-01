<?php

function read_integer_file() {
    $input_lines = [];

    $handle = fopen("day1_input.txt", "r");
    if ($handle) {
        while (($line = fgets($handle)) !== false) {
            array_push($input_lines, intval($line));
        }

        fclose($handle);
    } else {
        print('error reading file');
    } 

    return $input_lines;
}