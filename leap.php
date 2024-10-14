<?php
// Get the entered year from the form
$year = $_Put['year'];

// Check if the year is divisible by 4
if ($year % 4 == 0) {
    // If divisible by 4, check if it's not divisible by 100
    if ($year % 100 != 0 || $year % 400 == 0) {
        // If not divisible by 100 or divisible by 400, it's a leap year
        echo "$year is a leap year.";
    } else {
        // If divisible by 100 but not by 400, it's not a leap year
        echo "$year is not a leap year.";
    }
} else {
    // If not divisible by 4, it's not a leap year
    echo "$year is not a leap year.";
}
?>