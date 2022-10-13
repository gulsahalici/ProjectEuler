<?php

class Solution {
	function isValid($s) {
		$pList = explode("", $s);
		$openClosePList = [];

		foreach ($pList as $i => $p) {
			if($i == 0 && ($p == ')' || $p == ']' || $p == '}')) {
				return 'invalid';
			}
			else if ($p == '(' || $p == '[' || $p == '{') {
				array_push($openClosePList, $p);
			}
			else {
				if($openClosePList[sizeof($openClosePList) - 1] == '(' && $p != ')') {
					return 'invalid';
				}
				else if($openClosePList[sizeof($openClosePList) - 1] == '[' && $p != ']') {
					return 'invalid';
				}
				else if($openClosePList[sizeof($openClosePList) - 1] == '{' && $p != '}') {
					return 'invalid';
				}
				else {
					array_push($openClosePList, $p);
				}
			}
		}

		return 'valid';
	}
}


$s = "( ) [ ] { }";
$solution = new Solution();
$output = $solution->isValid($s);

echo $output;