<?php

function web_test($url,$tiempo){

	$check = @fsockopen($url, 80, $errno, $errstr, $tiempo);

	if(!$check) echo "Offline Web: $url \r\n";

	fclose($check);

}

?>
