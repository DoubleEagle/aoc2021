<?php 

include('../utility.php');

$input_array = read_integer_file('day1_input.txt');

function number_increase_decrease_same($numbers) {
    $increase = 0;
    $decrease = 0;
    $same = 0;
    for($i = 1; $i < count($numbers); $i++) {
        if($numbers[$i] - $numbers[$i-1] > 0) {
            $increase++;
        }
    }
    return $increase;
}

function sliding_window_increased($numbers) {
    $increased = 0;
    $prev_sum = 0;

    for($i = 2; $i < count($numbers); $i++) {
        $sum = $numbers[$i - 2] + $numbers[$i - 1] + $numbers[$i];
        if($i != 2 && $sum > $prev_sum) {
            $increased++;
        }
        $prev_sum = $sum;
    }

    return $increased;
}

var_dump(sliding_window_increased($input_array));


?>