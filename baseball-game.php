<?php
/**
 * 
 */
class Solution {
	
	function callPoints($ops)
	{
		$output = array();

		foreach ($ops as $opt) {
			if($opt == 'C') {
				array_pop($output);
			}
			else if($opt == 'D') {
				array_push($output, end($output) * 2);
			}
			else if($opt == '+') {
				array_push($output, $output[sizeof($output) - 1] + ($output[sizeof($output) - 2]));
			}
			else {
				array_push($output, strval($opt));
			}
		}

		$sum = 0;

		foreach ($output as $o) {
			$sum = $sum + $o;
		}

		return $sum;
	}
}

// read inputs
$ops = explode(' ', "5 2 C D +");

// Solution
$solution = new Solution();
$output = $solution->callPoints($ops);

//print the output
echo $output;